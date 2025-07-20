from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import BlogPost 
import os
from django.db.models import F

# Create your views here.

def homePage(request):
    blogpost = BlogPost.objects.all().order_by("-create_at")
    if request.method == "POST":
        query = request.POST["query"]
        checkquery = BlogPost.objects.filter(user__username = query).exists()
        if checkquery == True:
            blogpost = BlogPost.objects.filter(user__username = query)
            return render(request, "tweet_home.html", {"blogpost":blogpost})
        else:
            messages.warning(request, "No post exists")
            return render(request, "tweet_home.html", {"blogpost":blogpost})
    return render(request, "tweet_home.html", {"blogpost":blogpost})

def viewIndex(request):
    return redirect(homePage)

@login_required()
def createTweet(request):
    if request.method == "POST":
        username = request.user
        title = request.POST["title"]
        text = request.POST["text"]
        image = request.FILES["image"]

        post = BlogPost.objects.create(user=username, title=title, text=text, image=image)
        post.save()
        return redirect(homePage)
    return render(request, "create_tweet.html")

def editTweet(request, blogId):
    blog = BlogPost.objects.get(id=blogId)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.text = request.POST["text"]
        try:
            if request.FILES["image"] != "":
                image_path = blog.image.path
                os.remove(image_path)
                blog.image = request.FILES["image"]
        except(KeyError):
            blog.image = blog.image
        blog.save()
        return redirect('homePage')
    return render(request, "edit_tweet.html", {"blog":blog})

def seeTweet(request, blogId):
    blog = BlogPost.objects.get(id=blogId)
    return render(request, "see_tweet.html", {"blog":blog})

def deleteTweet(request, blogId):
    blog = BlogPost.objects.get(id=blogId)
    image_path = str(blog.image.path)
    blog.delete()
    if os.path.isfile(image_path):
        os.remove(image_path)
    return redirect('homePage')

'''def UserRegister(request):
    form = None
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('homePage')
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form":form})'''

def UserRegister(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        check_user = User.objects.filter(username=username).exists()
        if check_user == True:
            messages.warning(request, "user already exists")
            return render(request, "registration/register.html")
        user = User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect(homePage)
    return render(request, "registration/register.html")

        
def UserLogin(request):
    form = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print("user not found")
    return render(request, "registration/login.html")

def UserLogout(request):
    logout(request)
    return redirect("/tweet/register/")