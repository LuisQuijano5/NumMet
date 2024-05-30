import sys
from PySide6 import QtWidgets, QtGui, QtCore
from View.InterpolacionLinealView import MainWindow  # Asegúrate de importar la vista correctamente

class InterpolacionLinealController:
    def __init__(self, app):
        self.app = app
        self.ventana = MainWindow()
        self.ventana.show()

        # Conectar eventos de la interfaz gráfica a la lógica
        self.ventana.button_calcular.clicked.connect(self.calcular)
        self.ventana.button_volverMenu.clicked.connect(self.return_to_menu)
        self.ventana.button_a.clicked.connect(self.show_help)

        # Variables para almacenar los valores ingresados
        self.x = None
        self.fx = None
        self.x0 = None
        self.fx0 = None
        self.x1 = None
        self.fx1 = None

    def calcular(self):
        # Obtener los valores ingresados y almacenarlos en las variables
        try:
            self.x = float(self.ventana.edit_x_IL.text())
            self.fx = float(self.ventana.edit_fx_IL.text())
            self.x0 = float(self.ventana.edit_x0_IL.text())
            self.fx0 = float(self.ventana.edit_fx0_IL.text())
            self.x1 = float(self.ventana.edit_x1_IL.text())
            self.fx1 = float(self.ventana.edit_fx1_IL.text())

            new_fx = self.fx0 + (((self.fx1 - self.fx0) / (self.x1 - self.x0))*(self.x - self.x0))
            new_fx = round(new_fx, 6)

            self.ventana.edit_resultado.setText(str(new_fx))

            #error
            ep = abs((self.fx - new_fx) / self.fx) * 100
            ep = round(ep, 6)

            self.ventana.edit_error.setText(str(ep))

        except ValueError:
            self.ventana.show_error_message("Por favor, ingresa valores válidos en todos los campos.")

        print(self.x, self.fx, self.x0, self.fx0, self.x1, self.fx1)

        def limpiar_campos(self):
            # Llamar a la función de la ventana para limpiar los campos
            self.ventana.limpiar_campos()


    def return_to_menu(self):
        # Lógica para volver al menú principal
        from MainController import MainController
        self.main_controller = MainController()
        self.main_controller.show_menu()
        self.ventana.close()

    def show_help(self):
        # Lógica para mostrar el diálogo de ayuda
        help_dialog = QtWidgets.QDialog()
        help_dialog.setWindowTitle("Manual de Usuario Interpolación Lineal")
        help_dialog.setFixedSize(650, 400)

        layout = QtWidgets.QVBoxLayout()

        # Título
        title_label = QtWidgets.QLabel("Manual de Usuario Interpolación Lineal")
        title_label.setStyleSheet("font-family: Arial, sans-serif; font-size:14pt;")
        layout.addWidget(title_label)

        # Instrucciones
        instructions_label = QtWidgets.QLabel(
            "Instrucciones para utilizar la Interpolación Lineal...\n"
            "La primera casilla, x, es el valor que se calculara con los otros dos valores, f(x) se usa para el error\n\n"
            "Ejemplo de cómo ingresar los valores:\n\n"
            "x: 1.5\n"
            "f(x): 2.3\n"
            "x_0: 1.0\n"
            "f(x_0): 2.0\n"
            "x_1: 2.0\n"
            "f(x_1): 3.0\n\n"
            "La fórmula usada para calcular la aproximación es la siguiente:\n\n"
            "                        f(x_1) - f(x_0)\n"
            "f(x) = f(x_0) + -------------------- (x - x_0)\n"
            "                           x_1 - x_0\n\n"
            "***Tenga cuidado de que sus valores en x_1 y x_0 no resulten en división por 0."
        )
        instructions_label.setStyleSheet("font-family: Arial, sans-serif; font-size:11pt;")
        layout.addWidget(instructions_label)

        # Botón de regresar
        return_button = QtWidgets.QPushButton("Return")
        return_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;")
        return_button.clicked.connect(help_dialog.close)
        layout.addWidget(return_button)

        help_dialog.setLayout(layout)
        help_dialog.exec()


    def move_window_to_center(self):
        # Mover la ventana al centro de la pantalla
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.ventana.width()) / 2
        y = (screen_geometry.height() - self.ventana.height()) / 2
        self.ventana.move(x, y)

    def run(self):
        sys.exit(self.app.exec())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = InterpolacionLinealController()
    controller.run()
