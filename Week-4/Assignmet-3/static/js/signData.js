const form = document.querySelector('form')
const signUpButton = document.querySelector('.signUp input[type="submit"]')
const signUpErrorMessage = document.querySelector('.errorReturnMessage')
const email = document.querySelector('input[name="email"]')
const password = document.querySelector('input[name="password"]')
signUpButton.style.backgroundColor = 'red';

form.addEventListener('submit',(e)=>{
    e.preventDefault()
})

signUpButton.addEventListener('click',() =>{
    emailValue = email.value
    passwordValue = password.value
    fetch('/checksignin', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({'email': emailValue, 'password': passwordValue})
}   )
    .then(response => {
        return response.json()
    })
    .then(json => {
        console.log(json['message'])
        if (json['message'] === "Access Success"){
            window.location.href = '/welcomePage?email='+emailValue ;
        }
        else if (json['message'] === "Email already Exist"){
            signUpErrorMessage.innerText = "Email already Exist"
        }
        // else if (json['message'] === "Email or Password is wrong ! "){
        //     signInErrorMessage.innerText = "Email or Password is wrong !"
        // }
    })


})







