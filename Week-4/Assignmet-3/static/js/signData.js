const form = document.querySelectorAll("form");
const email = document.querySelectorAll('input[name="email"]');
const password = document.querySelectorAll('input[name="password"]');
const errorMessage = document.querySelector('.errorReturnMessage');

function setAction(message, email) {
    switch(message) {
        case 'Access Success':
            window.location.href = '/welcomePage?email='+ email;
            break;
        case 'Email already Exist':
            errorMessage.innerText = "Email already Exist , please try to Sign In your Account.";
            break;
        case 'Email or Password is wrong ! ':
            errorMessage.innerText = "Email or Password is wrong !";
            break;
        default:
            break;
    }
}

function fetchUser(email, password, status) {
    // 將資料送傳到後端，來做後續資料庫的比對與建檔
    fetch('/checkSignSituation', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({email, password, status })
    })
    // 後端會根據資料，給予相對應的訊息回前端
    .then(response => {
        return response.json()
    })
    .then(json => {
        setAction(json['message'], email)
    })
}

form.forEach( form => {
    form.addEventListener('submit',(e) =>{
        // 將 form 預設的 submit 效果移除
        e.preventDefault();       
        // 找出哪一個按鈕被點擊
        let status = e.target.id
        let emailValue ;
        let passwordValue ;
        // 根據點擊的按鈕，找出相對應的 Email and Password （這邊應該可以用更好的寫法）
        if (status =="signUp"){
            emailValue = email[0].value
            passwordValue = password[0].value
            console.log(emailValue)
        }
        else if(status =="signIn"){
            emailValue = email[1].value
            passwordValue = password[1].value
            console.log(emailValue)            
        }
        fetchUser(emailValue, passwordValue, status)
    })
})






