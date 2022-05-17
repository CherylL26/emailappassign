from flask import Flask, request
from flask_mail import Mail, Message
app = Flask(__name__)

mailconf = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'webdevtesting24@gmail.com',
    "MAIL_PASSWORD": 'njvmbwyamollqmxw'
}
app.config.update(mailconf)
mail = Mail(app)

@app.route("/", methods = ['POST'])
def main():
    data = request.get_json()
    to = data['to']
    subject = data['subject']
    body = data['body']
    msg = Message(subject, sender=app.config.get("MAIL_USERNAME"), recipients=[to])
    msg.body = body
    mail.send(msg)
    return '''
    to: {}
    subject: {}
    body: {}'''.format(to, subject, body)