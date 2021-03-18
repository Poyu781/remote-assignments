const form = document.querySelectorAll("form");
const email = document.querySelectorAll('input[name="email"]');
const password = document.querySelectorAll('input[name="password"]');
const errorMessage = document.querySelector('.errorReturnMessage');

form.forEach( form => {
    form.addEventListener('submit',(e) =>{
        // 將 form 預設的 submit 效果移除
        e.preventDefault();
        
        // 找出哪一個按鈕被點擊
        let action = e.target.id
        let emailValue ;
        let passwordValue ;

        // 根據點擊的按鈕，找出相對應的 Email and Password （這邊應該可以用更好的寫法）
        if (action =="signUp"){
            emailValue = email[0].value
            passwordValue = password[0].value
            console.log(emailValue)
        }
        else if(action =="signIn"){
            emailValue = email[1].value
            passwordValue = password[1].value
            console.log(emailValue)            
        }
        // 原本不是用 form 格式時，拿來判斷是否沒有輸入就點擊，後改成 form 後則不需要了
        // if (emailValue === "" | passwordValue === ""){
        //     errorMessage.innerText = "Please Enter Email and Password"
        //     return "wrong input" }

        // 將資料送傳到後端，來做後續資料庫的比對與建檔
        fetch('/checkSignSituation', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'email': emailValue, 'password': passwordValue, "status": action })
        })
        // 後端會根據資料，給予相對應的訊息回前端
        .then(response => {
            return response.json()
        })
        .then(json => {
            console.log(json['message'])
            // 註冊成功與登入成功，將跳轉至 Welcome Page
            if (json['message'] === "Access Success"){                
                window.location.href = '/welcomePage?email='+emailValue ;
            }
            // 如果 Sign Up 時發現此 Email 已經在資料庫，則回傳下方資訊
            else if (json['message'] === "Email already Exist"){                
                errorMessage.innerText = "Email already Exist , please try to Sign In your Account."
            // 如果 Sign In 時發現輸入資料無法與資料庫匹配，則回傳下方資訊
            // 這次練習讓我知道，為什麼有些登入畫面都寫[帳號或密碼錯誤]，而不是某一個對了但某一個錯了，原來就是懶啊哈哈
            }
            else if (json['message'] === "Email or Password is wrong ! "){                
                errorMessage.innerText = "Email or Password is wrong !"

            }
        })
    })
})




