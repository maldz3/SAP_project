from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<int:number>')
def all_integers(number):
    arr = []
    for i in range(1, number+1):
        arr.append(i)

    return render_template('integers.html', num_list=arr)


@app.route('/<int:number>/odd')
def odd_integers(number):
    arr = []
    for i in range(1, number+1, 2):
        arr.append(i)

    return render_template('integers.html', num_list=arr)


@app.route('/<int:number>/even')
def even_integers(number):
    arr = []
    if number > 1:
        for i in range(2, number+1, 2):
            arr.append(i)

    return render_template('integers.html', num_list=arr)


@app.route('/<int:number>/prime')
def prime_integers(number):
    arr = []
    for i in range(2, number+1):
        if is_prime(i):
            arr.append(i)

    return render_template('integers.html', num_list=arr)


def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    app.run()
