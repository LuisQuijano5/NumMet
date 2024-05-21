class Lineal_Interpolation_Solver:
    def __init__(self):
        self.f_x = None
        self.x = None
        self.x_zero = None
        self.x_one = None
        self.f_x_zero = None
        self.f_x_one = None

    def ask_user_input(self):
        f_x = float(input("Introduce el valor de f(x): "))
        x = float(input("Introduce el valor de x donde deseas evaluar la función interpolada: "))
        x_zero = float(input("Introduce el valor de x_zero (punto inicial): "))
        f_x_zero = float(input("Introduce el valor de f(x_cero): "))
        x_one = float(input("Introduce el valor de x_one (punto final): "))
        f_x_one = float(input("Introduce el valor de f(x_uno): "))

        return f_x, x_zero, x_one, x, f_x_zero, f_x_one

    def init(self, f_x, x_zero, x_one, x, f_x_zero, f_x_one):
        # Inicializar la función y los valores iniciales
        self.f_x = f_x
        self.x = x
        self.x_zero = x_zero
        self.x_one = x_one
        self.f_x_zero = f_x_zero
        self.f_x_one = f_x_one

    def calculate(self):
        f_x_zero = round(self.f_x_zero, 6)

        f_x_one = round(self.f_x_one, 6)

        f_x = round(self.f_x, 6)

        # Calcular con fórmula
        f_new_x = f_x_zero + (((f_x_one - f_x_zero) / (self.x_one - self.x_zero)) * (self.x - self.x_zero))
        f_new_x = round(f_new_x, 6)
        print(f"Valor interpolado de la función en x: {f_new_x}")

        #Calcular error
        ep = abs((f_x - f_new_x) / f_x) * 100
        ep = round(ep, 6)
        print(f"Valor del error es: {ep}")


# Ejemplo de uso
solver = Lineal_Interpolation_Solver()
f_x, x_zero, x_one, x, f_x_zero, f_x_one = solver.ask_user_input()
solver.init(f_x, x_zero, x_one, x, f_x_zero, f_x_one)
solver.calculate()