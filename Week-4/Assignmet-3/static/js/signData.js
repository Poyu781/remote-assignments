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

function fetchUser(url, email, password) {
    // 將資料送傳到後端，來做後續資料庫的比對與建檔
    fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({email, password })
    })
    // 後端會根據資料，給予相對應的訊息回前端
    .then(response => {
        return response.json()
    })
    .then(json => {
        setAction(json['message'], email)
    })
}

document.addEventListener('submit', (e) => {
    e.preventDefault()
    const form = e.target
    console.log('form_name', form.id)
    const email = form.querySelector('input[name="email"]').value
    const password = form.querySelector('input[name="password"]').value
    console.log({email, password})
    fetchUser(`/${form.id}`, email, password)
})








