from flask import Flask, render_template, request

app = Flask(__name__)


# renders index.html
@app.route('/')
def index():
    return render_template('index.html')


# updates second text field with processed input from text field 1 on submit button
@app.route('/', methods=['POST', 'GET'])
def get_user_input():
    text = request.form["user-input"]
    # this should be where text becomes rephrased
    processed_text = text.upper()
    return render_template('index.html', output=processed_text)


# only for testing purposes, we will need to delete before deployment
if __name__ == "__main__":
    app.run()
