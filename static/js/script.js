function togglelogin(id) {
    var tabs=(document.getElementsByClassName("slider"));
    var tabcontent=(document.getElementsByClassName("form-content"));

    // console.log(tabs)
    // console.log(tabcontent)
    // console.log(id,tabs,tabs[id],tabcontent,tabcontent[0],tabcontent[1],id,tabcontent[id])

    for (let i = 0; i < tabs.length; i++)
        tabs[i].classList.remove("tog-active");
    
    for (let i = 0; i < tabs.length; i++)
        tabcontent[i].style.display="none";

    // console.log(id,tabs[id],tabs)
    tabs[id].classList.add("tog-active");
    tabcontent[id].style.display="block"
}