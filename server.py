from flask import Flask, render_template, request
from typograf import process_text

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result_text():
    input_text = request.form['text']
    output_text = process_text(input_text)
    return render_template('form.html', input_text=input_text, output_text=output_text)


if __name__ == "__main__":
    app.run()
