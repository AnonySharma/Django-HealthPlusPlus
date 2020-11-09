
function togglelogin(id) {
    var tabs=(document.getElementsByClassName("slider"));
    var tabcontent=(document.getElementsByClassName("form-content"));

    for (let i = 0; i < tabs.length; i++)
        tabs[i].classList.remove("tog-active");
    
    for (let i = 0; i < tabs.length; i++)
        tabcontent[i].style.display="none";

    tabs[id].classList.add("tog-active");
    tabcontent[id].style.display="block"
}