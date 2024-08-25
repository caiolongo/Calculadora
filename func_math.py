class MathFunc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def minusModule(x, y):
        if (x > y):
            return x - y
        else:
            return y - x

    def multiply(x, y):
        return x * y
    
    def division(x, y):
        return x / y

    def percent(x, y):
        return y * (x / 100)