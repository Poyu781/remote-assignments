function showGreet(){
    document.getElementById("welcome").innerHTML='Have a Good Time!';
}

function showMore() {
  const blocks = document.getElementById("hidden");

  if (blocks.style.display === "none"){
   
    blocks.style.display = "flex";
  } else {
    blocks.style.display = "none";
  }
}

document.querySelector('#welcome').addEventListener("click", showGreet)
document.querySelector('.button-container button').addEventListener("click", showMore)