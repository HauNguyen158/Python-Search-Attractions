$open = false;

document.getElementById("action_menu_btn").onclick = function () {
    document.getElementsByClassName("chat")[0].style.display = "none";
};


document.getElementById("open-chat").onclick = function () {
    // element.scrollIntoView
    if($open == false){
        document.getElementsByClassName("chat")[0].style.display = "block";
        $open =true;
    }
    else{
        document.getElementsByClassName("chat")[0].style.display = "none";
        $open =false;
    }
};
