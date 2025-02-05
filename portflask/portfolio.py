from flask import Flask,render_template,request, url_for, flash,redirect
from flask_mail import Mail, Message


app=Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # SMTP server
app.config['MAIL_PORT'] = 587  # Port for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'ak2072719@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'lxvj ccrl xkha ezfb'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = ('ak2072719@gmail.com')  # Sender info

mail = Mail(app)


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

@app.route('/contact_me',methods=['GET'])
def Contact_me():
     return render_template('contact.html')
@app.route('/contact',methods=['POST'])
def Contact():
        if request.method == "POST":
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['msg']

            # Create email message
            msg = Message(
                subject="Contact Form Submission",
                recipients=['ak2072719@gmail.com'],  # Recipient email
                body=f"Name: {name}\nEmail: {email}\nPhone :{phone} \nMessage: {message}"
            )
            print(name,email,message)
            try:
                mail.send(msg)  # Send the email
                flash("!! Thank You for your response. I will connect with you ASAP !!", "success")
            except Exception as e:
                print(f"Error: {e}")
                flash("Failed to send message. Please try again.", "danger")

        return redirect(url_for('Contact_me'))


app.run()