from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<int:number>')
def all_integers(number):
    string = ""
    for i in range(1, number+1):
        string += str(i) + " "
    return string


@app.route('/<int:number>/odd')
def odd_integers(number):
    string = ""
    for i in range(1, number+1, 2):
        string += str(i) + " "
    return string


@app.route('/<int:number>/even')
def even_integers(number):
    string = ""
    if number > 1:
        for i in range(2, number+1, 2):
            string += str(i) + " "
    return string


@app.route('/<int:number>/prime')
def prime_integers(number):
    string = ""
    for i in range(2, number+1):
        if is_prime(i):
            string += str(i) + " "
    return string


def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    app.run()
