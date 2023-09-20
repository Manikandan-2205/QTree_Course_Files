from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def corse():
    return render_template('index.html')


@app.route('/Manikandan')
def details():
    return render_template('manikandan.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
