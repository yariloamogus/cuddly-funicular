from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/korea')
def korea():
    return render_template('main.html')


@app.route('/iran')
def idian():
    return render_template('iran.html')


@app.route('/kavkaz')
def kavkaz():
    return render_template('kavkaz.html')


@app.route('/turkey')
def turkey():
    return render_template('turkey.html')


if __name__ == '__main__':
    app.run(debug=True  )