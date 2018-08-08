from flask import Flask, render_template, request
from typograf import edit_text

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        input_text = request.form.get('text')
        result_text = edit_text(input_text)
        return render_template('form.html', result_text=result_text, input_text=input_text)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
