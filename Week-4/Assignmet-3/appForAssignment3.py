from flask import (Flask, render_template, flash,
request,url_for,redirect,make_response)
import json
import pymysql.cursors

app = Flask(__name__)
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root123',
                            database='assignment',
                            cursorclass=pymysql.cursors.DictCursor)

@app.route("/")
def home():
    return "Hello"

@app.route('/homePage',methods=["POST", "GET"])
def sign_page(): 
    return render_template("Assignment3.html")

@app.route('/checksignin', methods = ["POST","GET"])
def check_sign_up():
    
    data = request.get_json()
    print("1")
    print(data["email"], data["password"])

    connection.connect()

    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql_search =  "SELECT id, email  FROM test WHERE email = %s"
            cursor.execute(sql_search,(data['email'],))
            if cursor.fetchone() :
                # 加一個訊息，說這個 email 已經用過了
                text = {"message" : "Email already Exist"}
                print(text)
                return json.dumps(text)
            else:
                sql_input = "INSERT INTO test (email, password) VALUES (%s, %s)"
                cursor.execute(sql_input, (data['email'], data['password']))
                connection.commit()
                connection.close
                text = {"message" : "Access Success"}
                print(text)
                return json.dumps(text)
                
        
        
    
    

@app.route('/welcomePage', methods = ["POST","GET"])
def welcomePage(email=None):
    email = request.args.get('email', email)
    return f"hello, {email} ! Nice to meet you !"


if __name__ == "__main__":
    app.run(debug= True,port=5000)



