document.querySelector('.button').addEventListener("click", ()=>{
  const data = document.querySelector('input[name="number"]').value
  document.querySelector('.input').innerHTML = data
  document.querySelector('input[name="number"]').value = ''
  
  const request = new XMLHttpRequest()
  request.onload = function(){
    if (request.status >= 200 && request.status< 400){
      const result = request.responseText
      const span = document.querySelector(".answer")
      span.innerHTML = result
    } else {
      console.log('err')
    }
  }
  request.onerror = function(){
    console.log('error')
  }
  request.open('GET',`http://127.0.0.1:3000/data?number=${data}`,true)
  request.send()
})



// const request = new XMLHttpRequest()
// request.onload = function(){
// if (request.status >= 200 && request.status< 400){
//   console.log(request.responseText)
//   const result = request.responseText
//   const span = document.querySelector(".answer")
//   span.innerHTML = result
//   } else {
//     console.log('err')
//   }

// }
// request.onerror = function(){
//   console.log('errpr')
// }
// request.open('GET',`http://127.0.0.1:3000/data?number=${data}`,true)
// request.send()