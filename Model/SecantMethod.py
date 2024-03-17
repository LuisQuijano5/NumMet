from .Equation_Solver import Function

class SecantSolver:
    def __init__(self):
        self.function = None
        self.error = None
        self.xi_minus_1 = None
        self.xi = None

    def init(self, expression_function, error, xi_minus_1, xi):
        # Inicializar la función y los valores iniciales
        self.function = Function(expression_function)
        self.error = error
        self.xi_minus_1 = xi_minus_1
        self.xi = xi

    def calculate_next_approximation(self):
        # Calcular la siguiente aproximación utilizando la ecuación de la secante
        f_xi_minus_1 = self.function.evaluate(self.xi_minus_1)
        f_xi = self.function.evaluate(self.xi)

        # Evitar la división por cero verificando si los valores de la función son cero
        if abs(f_xi - f_xi_minus_1) < 1e-10:
            raise ValueError("La función es casi constante en el intervalo, no se puede continuar.")

        xi_plus_1 = self.xi - (f_xi * (self.xi_minus_1 - self.xi) / (f_xi_minus_1 - f_xi))

        # Calcular el error porcentual aproximado
        approximate_error = abs((xi_plus_1 - self.xi) / xi_plus_1) * 100

        # Verificar si el denominador en el cálculo del error es cercano a cero, lo que indica posible divergencia
        if abs(f_xi_minus_1 - f_xi) < 1e-10:
            raise ValueError("Posible divergencia: El denominador en el cálculo del error es cercano a cero.")

        return xi_plus_1, approximate_error

    def solve(self):
        try:
            while True:
                xi_plus_1, approximate_error = self.calculate_next_approximation()

                # Redondear los valores a 6 decimales
                xi_plus_1 = round(xi_plus_1, 6)
                approximate_error = round(approximate_error, 6)

                print(f"xi_minus_1: {self.xi_minus_1}, xi: {self.xi}")
                print(f"Siguiente aproximación (x): {xi_plus_1}")
                print(f"Error porcentual aproximado: {approximate_error}%\n")

                # Verificar si la nueva aproximación cumple con el criterio de error establecido
                if approximate_error <= self.error:
                    print("¡La aproximación cumple con el criterio de error establecido!")
                    break

                # Actualizar valores para la próxima iteración
                self.xi_minus_1 = self.xi
                self.xi = xi_plus_1

        except ValueError as e:
            print("Error:", e)
            print("No es posible resolver la ecuación debido a un problema identificado.")
