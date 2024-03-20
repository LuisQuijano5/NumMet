import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QDialog, QWidget, QVBoxLayout, QPushButton, QScrollArea

from Model.Bisection_Method import Bisection_Method
from View.BiseccionView import MainWindow
from Model.Equation_Solver import Function
import sympy as sp

class BisectionController:
    def __init__(self, app):
        self.app = app
        self.ventana = MainWindow()
        self.ventana.show()

        # Conectar eventos de la interfaz gráfica a la lógica
        self.ventana.button_calcular.clicked.connect(self.calcular)
        self.ventana.button_graficar.clicked.connect(self.graficar)
        self.ventana.button_volverMenu.clicked.connect(self.return_to_menu)
        self.ventana.button_a.clicked.connect(self.help)

        # Crear una instancia del solucionador de la ecuación
        self.solver = Bisection_Method()

    def calcular(self):
        try:
            expression_function = self.ventana.edit_ecuacion.text()
            error = float(self.ventana.edit_error.text())
            xi_minus_1 = float(self.ventana.edit_a.text())
            xi = float(self.ventana.edit_b.text())

            # Verificar si la expresión es una función válida
            if not self.is_valid_function(expression_function):
                raise ValueError("La expresión ingresada no es una función válida.")

            # Limpiar la tabla antes de agregar nuevos resultados
            self.ventana.tabla_resultados.clearContents()
            self.ventana.tabla_resultados.setRowCount(0)

            # Inicializar el solucionador con los valores ingresados
            #self.solver.init(expression_function, error, xi_minus_1, xi)

            # Resolver la ecuación y obtener los resultados

            solver_results, error_message = self.solver.iteration(expression_function, error, xi_minus_1, xi)


            # Agregar los resultados a la tabla
            for i, (xi_minus_1, xi, f_xi_minus_1, f_xi, xi_plus_1,f_xi_plus_1, error) in enumerate(solver_results):
                self.ventana.tabla_resultados.insertRow(i)
                self.ventana.tabla_resultados.setItem(i, 0, QtWidgets.QTableWidgetItem(str(xi_minus_1)))
                self.ventana.tabla_resultados.setItem(i, 1, QtWidgets.QTableWidgetItem(str(xi)))
                self.ventana.tabla_resultados.setItem(i, 2, QtWidgets.QTableWidgetItem(str(f_xi_minus_1)))
                self.ventana.tabla_resultados.setItem(i, 3, QtWidgets.QTableWidgetItem(str(f_xi)))
                self.ventana.tabla_resultados.setItem(i, 4, QtWidgets.QTableWidgetItem(str(xi_plus_1)))
                self.ventana.tabla_resultados.setItem(i, 5, QtWidgets.QTableWidgetItem(str(f_xi_plus_1)))
                self.ventana.tabla_resultados.setItem(i, 6, QtWidgets.QTableWidgetItem(str(error)))

            # Mostrar el último resultado en el campo de texto
            if solver_results:
                self.ventana.edit_resultado.setText(str(solver_results[-1][4]))
            else:
                # No se pudieron calcular resultados, por lo que no hay nada que mostrar
                self.ventana.edit_resultado.setStyleSheet("color: red;")  # Color rojo
                self.ventana.edit_resultado.setText("No se pudo calcular debido a una entrada inválida.")

            if (error_message != None):
                if error_message.startswith("Posible divergencia") or error_message.startswith(
                        "La función es casi constante" or error_message.startswith("El cálculo de la siguiente")):
                    # Manejo específico para la excepción de posible divergencia
                    self.ventana.show_error_message(
                        error_message + "\n\nRevisa que tu función y tus valores iniciales sean correctos.")
                else:
                    # Otros errores
                    self.ventana.show_error_message(
                        "Error: No es posible resolver la ecuación debido a un problema identificado." + "\n\nRevisa que tu función y tus valores iniciales sean correctos.")
        except Exception as e:
            # Capturar la excepción de división por cero en la función y mostrar el mensaje de error
            self.ventana.show_error_message(str(e))

    def is_valid_function(self, expression):
        # Intentar crear una expresión SymPy con la cadena de entrada
        expr = sp.sympify(expression)
        # Verificar si la expresión contiene al menos una variable
        return bool(expr.free_symbols)

    def graficar(self):
        # Método para graficar la función
        expression_function = self.ventana.edit_ecuacion.text()
        function = Function(expression_function)

        # Obtener la ruta de la imagen generada
        ruta_imagen = function.plot()

        # Crear una nueva ventana para mostrar la gráfica
        ventana_grafica = QtWidgets.QMainWindow()
        ventana_grafica.setWindowTitle("Gráfica de la función")

        # Cargar la imagen y obtener sus dimensiones
        pixmap = QPixmap(ruta_imagen)
        ancho_imagen = pixmap.width()
        alto_imagen = pixmap.height()

        # Establecer el tamaño de la ventana según las dimensiones de la imagen
        ventana_grafica.setFixedSize(ancho_imagen, alto_imagen)

        # Crear un widget para mostrar la gráfica
        widget_grafica = QtWidgets.QWidget()
        layout_grafica = QtWidgets.QVBoxLayout()
        widget_grafica.setLayout(layout_grafica)
        ventana_grafica.setCentralWidget(widget_grafica)

        # Mostrar la imagen en la nueva ventana
        label_grafica = QtWidgets.QLabel()
        label_grafica.setPixmap(pixmap)
        layout_grafica.addWidget(label_grafica)

        # Mostrar la nueva ventana
        ventana_grafica.show()

    def return_to_menu(self):
        from MainController import MainController
        self.main_controller = MainController()
        self.main_controller.show_menu()
        self.ventana.close()

    def help(self):
        help_dialog = QDialog()
        help_dialog.setWindowTitle("Manual de Usuario Secante")
        help_dialog.setFixedSize(650, 400)

        scroll_area = QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        content_widget = QWidget()
        content_layout = QVBoxLayout()

        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Manual de Usuario Secante")
        title_label.setStyleSheet("font-family: Arial, sans-serif; font-size:14pt;;")
        content_layout.addWidget(title_label)

        # Instrucciones
        instructions_label = QLabel(
            "Verifica inicialmente tu función y valores iniciales (que se llegue a una raíz en el intervalo)\n"
            "para evitar que aparezcan errores. Al final hay un ejemplo de cómo escribir una función.\n\n"

            "OPERACIONES ALGEBRAICAS\n\n"

            "-Exponentes: x^2 se escibe como x**2\n"
            "-Multiplicacion: x*2\n"
            "-Division: x/2\n"
            "-Suma: x + 2\n"
            "-Resta: x - 2\n"
            "-Raíz Cuadrada: x**(1/2) o con sqrt(x)\n"
            "-Raíz Cúbica: x**(1/3) o con cbrt(x)\n"
            "-Raíz de cuanquier radical: x**(1/n)\n"
            "-Numero e: e^x -> exp(x)\n"
            "-Valor Absoluto: Abs(x)\n"
            "-Factorial: factorial(x)\n\n"
            "FUNCIONES LOGARÍTMICAS\n\n"
            "-Logaritmo: log(x,base)\n"
            "-Logaritmo natural: log(x)\n\n"

            "FUNCIONES TRIGONOMÉTRICAS\n\n"

            "-Seno: sin(x)\n"
            "-Coseno: cos(x)\n"
            "-Tangente: tan(x)\n"
            "-Arcoseno: asin(x)\n"
            "-Arcocoseno: acos(x)\n"
            "-Arcotangente: atan(x)\n"
            "-Cosecante: csc(x)\n"
            "-Secante: sec(x)\n"
            "-Cotangente: cot(x)\n"
            "-Arcocosecante: acsc(x)\n"
            "-Arcosecante: asec(x)\n"
            "-Arcocotangente: acot(x)\n\n"

            "FUNCIONES HIPERBOLÍCAS\n\n"

            "-Seno hiperbólico: sinh(x)\n"
            "-Coseno hiperbólico: cosh(x)\n"
            "-Tangente hiperbólica: tanh(x)\n"
            "-Arcoseno hiperbólico: asinh(x)\n"
            "-Arcocoseno hiperbólico: acosh(x)\n"
            "-Arcotangente hiperbólica: atanh(x)\n\n"

            "FUNCIONES ESPECIALES\n\n"

            "-Función Gamma: gamma(x)\n"
            "-Función Beta: beta(x,y)\n\n"

            "Nota: Se respeta la prioridad por paréntesis\n\n"

            "EJEMPLO.\n\n"

            "La ecuación x^4 - 2x^3 - 12x^2 + 16x - 40 se esribe como:\n"
            "\tx**4 - 2*x**3 - 12*x**2 + 16*x - 40\n"
        )
        instructions_label.setStyleSheet("font-family: Arial, sans-serif; font-size:11pt;")
        content_layout.addWidget(instructions_label)

        # Botón de regresar
        return_button = QPushButton("Return")
        return_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;")
        return_button.clicked.connect(help_dialog.close)
        content_layout.addWidget(return_button)
        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area)

        help_dialog.setLayout(layout)
        help_dialog.exec()

    def move_window_to_center(self):
        # Mover la ventana al centro de la pantalla
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.ventana.width()) / 2
        y = (screen_geometry.height() - self.ventana.height()) / 2
        self.ventana.move(x, y)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    controller = BisectionController()
    controller.run()