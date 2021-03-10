let number;
const button = document.querySelector('.button');
const outputNumber = document.querySelector('.outputNumber');
const input = document.querySelector('input[name="number"]');
const answer = document.querySelector(".answer");
// click
button.addEventListener("click", ()=>{
  number = input.value
  getSum(number)
  outputNumber.innerText = number
  input.value = ''
})

// call api
function getSum(number) {
  const request = new XMLHttpRequest()
  request.onload = function(){
    if (request.status >= 200 && request.status< 400){
      const result = request.responseText 
      answer.innerText = result
    } else {
      console.log('err')
    }
  }
  request.onerror = function(){
    console.log('error')
  }
  request.open('GET',`http://127.0.0.1:3000/data?number=${number}`,true)
  request.send()
}