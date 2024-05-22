import os
import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from View.MainWindow import MainWindow
from View.MenuMethodsWiindow import MainWindowMenu
from Controller.GaussJordan_Controller import GaussJordanController
from Controller.Secant_Controller import SecantController
from Controller.SeidelController import SeidelController
from Controller.Bisectioncontroller import BisectionController
from Controller.RegresionCuadraticaController import RegresionCuadraticaController
from Controller.InterpolacionLinealController import InterpolacionLinealController
from Controller.DiferenciasDivController import InterpolacionDiferenciasDivididasController


class MainController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.button_siguiente.clicked.connect(self.show_menu)

        self.menu = None

    def show_menu(self):
        # Cerrar la ventana de inicio
        self.main_window.close()

        # Mostrar el menú
        self.menu = MainWindowMenu()
        self.menu.show()
        self.menu.button_siguiente.clicked.connect(self.on_continuar_click)

    def on_continuar_click(self):
        if self.menu.opcion_1.isChecked():
            self.ejecutar_metodo("Bisección")
        elif self.menu.opcion_2.isChecked():
            self.ejecutar_metodo("Secante")
        elif self.menu.opcion_3.isChecked():
            self.ejecutar_metodo("Gauss-Jordan")
        elif self.menu.opcion_4.isChecked():
            self.ejecutar_metodo("Gauss-Seidel")
        elif self.menu.opcion_5.isChecked():
            self.ejecutar_metodo("Regresion Cuadratica")
        elif self.menu.opcion_6.isChecked():
            self.ejecutar_metodo("Interpolacion Lineal")
        elif self.menu.opcion_7.isChecked():
            self.ejecutar_metodo("Interpolacion Diferencias Divididas")

    def ejecutar_metodo(self, metodo):
        # Cerrar el menú principal
        self.menu.close()
        # Mostrar la ventana correspondiente al método seleccionado
        if metodo == "Bisección":
            self.secant_controller = BisectionController(self)
            self.secant_controller.ventana.show()
            self.secant_controller.move_window_to_center()
            pass
        elif metodo == "Secante":
            self.secant_controller = SecantController(self)
            self.secant_controller.ventana.show()
            self.secant_controller.move_window_to_center()
            pass
        elif metodo == "Gauss-Jordan":
            self.controller = GaussJordanController(self)
            self.controller.view.show()
            self.controller.move_window_to_center()
            pass
        elif metodo == "Gauss-Seidel":
            self.controller_seidel = SeidelController(self)
            self.controller_seidel.view.show()

            pass
        elif metodo == "Regresion Cuadratica":
            self.controller_regresion_cuadratica = RegresionCuadraticaController(self)
            self.controller_regresion_cuadratica.ventana.show()
            self.controller_regresion_cuadratica.move_window_to_center()
            pass
        elif metodo == "Interpolacion Lineal":
            self.controller_lineal = InterpolacionLinealController(self)
            self.controller_lineal.ventana.show()
            self.controller_lineal.move_window_to_center()
            pass
        elif metodo == "Interpolacion Diferencias Divididas":
            self.controller_divididas = InterpolacionDiferenciasDivididasController (self)
            self.controller_divididas.ventana.show()
            self.controller_divididas.move_window_to_center()
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainController()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_dir, 'logoMETNUM.png')
    icon = QIcon(icon_path)

    app.setWindowIcon(icon)
    sys.exit(app.exec())