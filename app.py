from flask import Flask, render_template
#__name__ is already defined in any Python script
print(__name__)
app = Flask(__name__)  #create flask application

JOBS = [{
    'id': 1,
    'Title': 'Data Analyst',
    'Location': 'Bengaluru, India',
    'Salary': '10,00,000'
}, {
    'id': 2,
    'Title': 'Data Scientist',
    'Location': 'Delhi, India',
    'Salary': '12,00,000'
}, {
    'id': 3,
    'Title': 'Frontend Engineer',
    'Location': 'Remote',
    'Salary': '8,00,000'
}, {
    'id': 4,
    'Title': 'Backend Engineer',
    'Location': 'San Francisco, India',
    'Salary': '$120,000'
}]


@app.route("/")  #rootpage/homepage URL
#returns below function
# When root page is accessed, return "Hello, World"
def hello_world():
    #return "Hello, World"
    return render_template("home3.html", jobs=JOBS, company_name='Jovian')


if __name__ == "__main__":
    print("I'm inside if now !!")
    #'0.0.0.0' is local development server
    app.run(host='0.0.0.0', debug=True)  #START the app
