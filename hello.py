from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def get_user_input():
    text = request.form["user-input"]
    processed_text = text.upper()
    return render_template('index.html', output=processed_text)


if __name__ == "__main__":
    app.run()
