function ShowGreet(){
    document.getElementById("welcome").innerHTML = 'Have a Good Time!';
}

function ShowMore() {
    var blocks = document.getElementById("hidden");

    if (blocks.style.display === "none"){   
        blocks.style.display = "flex";
    } 
    else {
        blocks.style.display = "none";
    }
}