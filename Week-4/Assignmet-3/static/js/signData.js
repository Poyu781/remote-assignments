const button = document.querySelectorAll('input[type="submit"]')
const errorMessage = document.querySelector('.errorReturnMessage')
const email = document.querySelectorAll('input[name="email"]')
const password = document.querySelectorAll('input[name="password"]')


button.forEach( button => {
    button.addEventListener('click',() =>{
        let action = button.value ;
        let emailValue ;
        let passwordValue ;

        if (action =="Sign Up"){
            emailValue = email[0].value
            passwordValue = password[0].value
        }
        else if(action =="Sign In"){
            emailValue = email[1].value
            passwordValue = password[1].value            
        }

        if (emailValue === "" | passwordValue === ""){
            errorMessage.innerText = "Please Enter Email and Password"
            return "wrong input" }
        fetch('/checkSignSituation', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'email': emailValue, 'password': passwordValue, "status": action })
        })
        .then(response => {
            return response.json()
        })
        .then(json => {
            console.log(json['message'])
            if (json['message'] === "Access Success"){
                window.location.href = '/welcomePage?email='+emailValue ;
            }
            else if (json['message'] === "Email already Exist"){
                
                errorMessage.innerText = "Email already Exist , please try to Sign In your Account."

            }
            else if (json['message'] === "Email or Password is wrong ! "){
                
                errorMessage.innerText = "Email or Password is wrong !"

            }
        })
    })
})





