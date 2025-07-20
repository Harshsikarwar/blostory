let menu_status = "none"

let sideMenu = document.getElementById("side_menu")
let menuBurger = document.querySelectorAll("#menuBurger")

menuBurger.forEach(menu => {
    menu.addEventListener("click",()=>{
        if(menu_status === "none"){
            sideMenu.style.setProperty("--posX","0px")
            menu_status = "block"
        }else{
            sideMenu.style.setProperty("--posX","1000px")
            menu_status = "none"
        }
    })
});