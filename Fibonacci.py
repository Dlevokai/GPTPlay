class Fibonacci:
    def __init__(self, n):
        self.n = n

    def print_sequence(self):
        a, b = 0, 1
        for i in range(self.n):
            print(a)
            a, b = b, a + b

# To use the class, create an object and call the print_sequence method
fib = Fibonacci(10)
fib.print_sequence()