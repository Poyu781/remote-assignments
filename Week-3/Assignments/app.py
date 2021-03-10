from flask import Flask, render_template
from flask import request,url_for,redirect,make_response
app = Flask(__name__)

# Assignment 1
@app.route('/')
def home():
    return "Hello, My Server"

# Assignment 2
@app.route('/data')
def search(number=None):
    number = request.args.get('number',number)
    if  number == None or len(number) == 0:
        return "Lack  Parameter"
    # 當 input 無法被轉化成 int 時，則執行 except 內的程式 
    try:
        output = 0
        for i in range(1,int(number)+1):
            output += i
        return str(output)            
    except:
        return "Wrong Parameter"

# Assignment 3
@app.route('/sum.html')
def sum():
    return render_template("Assignment3.html")

# Assignment 4 
@app.route('/myName')
def show_name():
    try:
        name = request.cookies.get('userID')
        return "User Name : " + name
    except:
        return redirect(url_for('username_input',name='使用者的輸入'))

# Get input
@app.route('/trackName',methods = ["POST", "GET"])
def username_input():
    return render_template("enterUserName.html")

# Set cookie
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == 'POST' :
        user = request.form['username']   
        resp = make_response(redirect(url_for("show_name")))
        resp.set_cookie('userID', user)   
        return resp


if __name__ == "__main__":
    app.run(debug= True,port=3000)


