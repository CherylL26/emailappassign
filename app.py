from flask import Flask, request
from flask_mail import Mail, Message
app = Flask(__name__)

mailconf = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'webdevtesting24@gmail.com',
    "MAIL_PASSWORD": '$@BFwYu72ucHu!'
}
app.config.update(mailconf)
mail = Mail(app)

@app.route("/", methods = ['POST'])
def main():
    data = request.get_json()
    to = data['to']
    subject = data['subject']
    body = data['body']
    msg = Message('''{}
    
    {}'''.format(subject, body), sender=app.config.get("MAIL_USERNAME"), recipients=[to])
    mail.send(msg)
    return '''
    to: {}
    subject: {}
    body: {}'''.format(to, subject, body)