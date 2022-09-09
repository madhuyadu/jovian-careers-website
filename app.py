from flask import Flask, render_template
#__name__ is already defined in any Python script
print(__name__)
app = Flask(__name__)  #create flask application


@app.route("/")  #rootpage/homepage URL
#returns below function
# When root page is accessed, return "Hello, World"
def hello_world():
    #return "Hello, World"
    return render_template("home2.html")


if __name__ == "__main__":
    print("I'm inside if now !!")
    #'0.0.0.0' is local development server
    app.run(host='0.0.0.0', debug=True)  #START the app
