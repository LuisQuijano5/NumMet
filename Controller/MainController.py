import sys
import os
from PySide6 import QtWidgets

from View import MainWindow
from View import MenuMethodsWiindow

class MainController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        # Creamos las instancias de las ventanas
        self.main_window = MainWindow()
        self.menu_window = MenuMethodsWiindow()

        # Conectamos la señal del botón de la ventana principal a la función que muestra la segunda ventana
        self.main_window.button_siguiente.clicked.connect(self.mostrar_menu)

        # Mostramos la ventana principal
        self.main_window.show()

    def mostrar_menu(self):
        # Mostramos la ventana del menú de métodos
        self.menu_window.show()

if __name__ == "__main__":
    controller = MainController()
    sys.exit(controller.app.exec())
