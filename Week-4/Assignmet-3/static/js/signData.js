const signInClick = document.querySelector('.sigIn input[type="submit"]')
const email = document.querySelector('input[name="email"]')
const password = document.querySelector('input[name="password"]')
signInClick.addEventListener("click",() =>{
    emailValue = email.value
    passwordValue = password.value
    fetch("/checksignin", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"email": emailValue, "password": passwordValue})
}   )

})

console.log("d")

