from sympy import symbols, sympify

class MainModel:
    def __init__(self, a, b, ep):
        self.a = a
        self.b = b
        self.ep = ep

    def eval(self, x, eq):
        pass

    def getXr(self):
        self.xr = (self.a + self.b) / 2

