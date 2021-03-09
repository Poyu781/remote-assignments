from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, My Server"

@app.route('/data')
def search(number=None):
    number = request.args.get('number',number)
    if number == None :
        return "Lack  Parameter"
    try:
        output = 0
        for i in range(1,int(number)+1):
            output += i
        return str(output)
            
    except:
        return "Wrong Parameter"
@app.route('/sum.html')
def test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug= True,port=3000)


