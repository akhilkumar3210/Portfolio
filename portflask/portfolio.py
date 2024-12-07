from flask import Flask,render_template

app=Flask(__name__)

@app.route('/index',methods=['GET'])
def Index():
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def About():
    return render_template('about.html')

@app.route('/portfolio',methods=['GET'])
def Portfolio():
    return render_template('portfolio.html')

@app.route('/service',methods=['GET'])
def Service():
    return render_template('service.html')

@app.route('/contact',methods=['GET'])
def Contact():
    return render_template('contact.html')


app.run()