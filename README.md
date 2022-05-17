I hosted it on Heroku. All my code is in app.py.

You'll probably want to use Postman to send the POST request. The url is https://emailappassign.herokuapp.com/

Sample input (raw/JSON):

{
    "to": "your@email.com",
    "subject": "Hello World!",
    "body": "Email body here."
}
