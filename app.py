from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def main():
    data = request.get_json()
    to = data['to']
    subject = data['subject']
    body = data['body']
    return '''
    to: {}
    subject: {}
    body: {}'''.format(to, subject, body)