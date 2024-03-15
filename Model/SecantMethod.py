from Equation_Solver import Function

class SecantSolver:
    def __init__(self):
        self.function = None
        self.error = None
        self.xi_minus_1 = None
        self.xi = None

    def init(self):
        # Introducir la función y el valor inicial
        name_function = input("Introduzca el nombre de la función: ")
        expression_function = input("Introduzca la expresión de la función: ")
        self.function = Function(name_function, expression_function)

        # Introducir el valor máximo del error porcentual aproximado
        self.error = float(input("Introduzca el valor máximo del error porcentual aproximado: "))

        # Seleccionar dos aproximaciones iniciales xi-1 y xi
        self.xi_minus_1 = float(input("Introduzca el valor de xi-1: "))
        self.xi = float(input("Introduzca el valor de xi: "))

    def calculate_next_approximation(self):
        # Calcular la siguiente aproximación utilizando la ecuación de la secante
        f_xi_minus_1 = self.function.evaluate(self.xi_minus_1)
        f_xi = self.function.evaluate(self.xi)

        xi_plus_1 = self.xi - (f_xi * (self.xi_minus_1 - self.xi) / (f_xi_minus_1 - f_xi))

        # Calcular el error porcentual aproximado
        approximate_error = abs((xi_plus_1 - self.xi) / xi_plus_1) * 100

        return xi_plus_1, approximate_error, f_xi_minus_1, f_xi

    def solve(self):
        while True:
            xi_plus_1, approximate_error, f_xi_minus_1, f_xi = self.calculate_next_approximation()

            # Redondear los valores a 6 decimales
            xi_plus_1 = round(xi_plus_1, 6)
            approximate_error = round(approximate_error, 6)
            f_xi_minus_1 = round(f_xi_minus_1, 6)
            f_xi = round(f_xi, 6)

            print(f"xi_minus_1: {self.xi_minus_1}, xi: {self.xi}")
            print(f"f(xi_minus_1): {f_xi_minus_1}, f(xi): {f_xi}")
            print(f"Siguiente aproximación (x): {xi_plus_1}")
            print(f"Error porcentual aproximado: {approximate_error}%\n")

            # Verificar si la nueva aproximación cumple con el criterio de error establecido
            if approximate_error <= self.error:
                print("¡La aproximación cumple con el criterio de error establecido!")
                break

            # Actualizar valores para la próxima iteración
            self.xi_minus_1 = self.xi
            self.xi = xi_plus_1

# Aquí creamos una instancia de SecantSolver y resolvemos la ecuación
solver = SecantSolver()
solver.init()
solver.solve()
solver.function.plot()