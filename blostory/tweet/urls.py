from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('create-tweet/', views.createTweet, name="createTweet"),
    path('<int:blogId>/edit-tweet/', views.editTweet, name="editTweet"),
    path('<int:blogId>/see-tweet/', views.seeTweet, name="seeTweet"),
    path('<int:blogId>/delete-tweet/', views.deleteTweet, name="deleteTweet"),
    path('register/',views.UserRegister, name="userRegister"),
    path('accounts/logout/', views.UserLogout, name="userLogout"),
]