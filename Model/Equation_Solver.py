import sympy
from sympy import Symbol
import sympy as sym
import os

class Function:
    def __init__(self, expression):#Defines the function
        self.name = "f(x)"
        self.expression = sym.sympify(expression)
        self.x = Symbol("x")
        #self.error = error # %

    def evaluate(self, x):
        return self.expression.subs(sym.Symbol('x'), x)

    def plot(self):# Graph the Function
        plot_file = "grafica.png"
        sympy.plot(self.expression, title=f"Gráfica de {self.name}", show=False).save(plot_file)
        return os.path.abspath(plot_file)

class Application_Test:
    def __init__(self):
        self.function = None
        self.value_x = None
    def init(self):
        #Enter the function and the initial value
        expression_function = input("Introduzca la expresión de la función: ")
        self.function = Function(expression_function)#Stores object class Function
        # self.value_x = float(input("Introduzca el valor de x: "))  # Comentamos esta línea para evitar que se solicite el valor de x
    def show_result(self, value_x):  # Ahora aceptamos el valor de x como argumento
        result = self.function.evaluate(value_x)
        # Simplifica la expresión
        result = sympy.simplify(result)
        # Si la simplificación no elimina el logaritmo, convierte a número decimal
        if isinstance(result, sympy.Expr):
            result = sympy.N(result, 7)#Returns 6 decimal places after point
        print(f"El resultado de f({value_x}) es {result}")

# Aquí eliminamos el código que solicita y muestra el valor de x y el resultado de f(x)

# app = Application_Test()
# app.init()
# app.function.plot()
# app.show_result()
