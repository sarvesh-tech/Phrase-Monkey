from flask import Flask, render_template, request
import transformer

app = Flask(__name__)


# renders index.html
@app.route('/')
def index():
    return render_template('index.html')


# updates second text field with processed input from text field 1 on submit button
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    text = request.form["user-input"]
    # this should be where text becomes rephrased
    processed_text = transformer.paraphrase_text(text)
    return render_template('index.html', output=processed_text, input=text)


# only for testing purposes, we will need to delete before deployment
if __name__ == "__main__":
    app.run()
