from flask import Flask, render_template, request
import transformer

app = Flask(__name__)
char_lim = 300

# renders index.html
@app.route('/')
def index():
    return render_template('index.html')


# updates second text field with processed input from text field 1 on submit button
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    text = request.form["user-input"]
    # this should be where text becomes rephrased
    if len(text) < char_lim:
        processed_text = transformer.paraphrase_text(text)
    else:
        processed_text = "Too many characters! Currently, you are limited to " + str(char_lim) + \
                         " characters. Your text is " + str(len(text)) + " characters long."
    return render_template('index.html', output=processed_text, input=text)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/home')
def home():
    return render_template('index.html')
