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
  fetch(`http://127.0.0.1:3000/data?number=${number}`)
  .then((response) =>{
    return response.json()
  })
  .then(json => {
    answer.innerText = json["text"]
  })
}