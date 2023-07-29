# Building Url Dynamically
# Variable Rules And URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my Youtube Channel"


@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the marks is " + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is " + str(score)


# Result checker

@app.route('/results/<int:score>')
def results(score):
    result = ""
    if score < 50:
        result = 'fail'
    else:
        result = 'success'
    return result


if __name__ == '__main__':
    app.run(debug=True)
