from flask import (Flask, render_template, flash,
request,url_for,redirect,make_response)
import json
import pymysql.cursors

app = Flask(__name__)

# 建立連接資料庫資訊
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='assignment',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route("/")
def home():
    return "Hello"

@app.route('/home')
def home_page(): 
    return render_template("Assignment3.html")

# 前端回傳資料與資料庫互動
@app.route('/sign_up', methods = ["POST"])
def sign_up():
    # 從 Fetch 得到相對應的 data
    data = request.get_json()
    connection.connect()
    with connection:
        with connection.cursor() as cursor:
            sql_search =  "SELECT id, email  FROM user WHERE email = %s"
            cursor.execute(sql_search,(data['email'],))
            if cursor.fetchone() :
                text = {"message" : "Email already Exist"}
                return json.dumps(text)
            else:
                sql_input = "INSERT INTO user (email, password) VALUES (%s, %s)"
                cursor.execute(sql_input, (data['email'], data['password']))
                connection.commit()
                text = {"message" : "Access Success"}
                return json.dumps(text)


@app.route('/sign_in', methods = ["POST"])
def sign_in():
    data = request.get_json()
    connection.connect()
    with connection:
        with connection.cursor() as cursor:
            sql_search =  "SELECT id, email  FROM user WHERE email = %s and password = %s"
            cursor.execute(sql_search,(data['email'],data['password']))
            if cursor.fetchone() :
                text = {"message" : "Access Success"}
                return json.dumps(text)
            else:
                text = {"message" :"Email or Password is wrong ! "}
                return json.dumps(text)  



# 登入後的歡迎畫面
@app.route('/welcome', methods = ["POST","GET"])
def welcome_page(email=None):
    email = request.args.get('email', email)
    return f"hello, {email} ! Welcome !"


if __name__ == "__main__":
    app.run(debug= True,port=5000)



