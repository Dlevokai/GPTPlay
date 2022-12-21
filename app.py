from flask import Flask, request
from Fibonacci import Fibonacci
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/gptfibonacci')
def gpt_fibonacci():
    name = int(request.args.get('fibcount'))
    fib = Fibonacci(name)
    fib_ans = fib.print_sequence()
    return fib_ans

@app.route('/lovemultiplier')
def love_multiply():
    multiple = int(request.args.get('multiple'))
    random_int = random.randint(5, 10)
    new_str = "I love lauren at least " + str(random_int*multiple) + " times more than she loves me!"
    return new_str

if __name__ == '__main__':
    app.run()