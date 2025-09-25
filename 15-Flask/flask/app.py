from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask"

@app.route("/index")
def index():
    return "welcome to index"

if __name__=="__main__":
    app.run(debug=True)