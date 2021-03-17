from flask import Flask, render_template, flash
from flask import request,url_for,redirect,make_response
import json
app = Flask(__name__)

import pymysql.cursors
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root123',
                            database='user',
                            cursorclass=pymysql.cursors.DictCursor)
# Connect to the database
def interactive(data):
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql_search =  "SELECT id, email  FROM aa WHERE email = %s"
            cursor.execute(sql_search,(data['email'],))
            if cursor.fetchone() :
                # 加一個訊息，說這個 email 已經用過了
                return "already exist"
            else:
                sql_input = "INSERT INTO aa (email, password) VALUES (%s, %s)"
                cursor.execute(sql_input, (data['email'], data['password']))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        
        connection.commit()
    connection.connect()

@app.route('/')
def home():
    return "Hello, My Server"


@app.route('/Homepage',methods=["POST", "GET"])
def sign_page(): 
    return render_template("Assignment3.html")

@app.route('/checksignin', methods = ["POST","GET"])
def check_signin():

    data = request.get_json()
    print(data["email"], data["password"])
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql_search =  "SELECT id, email  FROM aa WHERE email = %s"
            cursor.execute(sql_search,(data['email'],))
            if cursor.fetchone() :
                # 加一個訊息，說這個 email 已經用過了
                return "already exist"
            else:
                sql_input = "INSERT INTO aa (email, password) VALUES (%s, %s)"
                cursor.execute(sql_input, (data['email'], data['password']))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        
        connection.commit()
    connection.connect()
    
    return "2"




if __name__ == "__main__":
    app.run(debug= True,port=5000)



