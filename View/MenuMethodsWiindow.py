import sys
from PySide6 import QtWidgets
from PySide6 import QtCore
import os

class MainWindowMenu(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccione una opción")
        self.setGeometry(100, 100, 800, 600)

        # Cargar los estilos CSS
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, 'styleSheet.css')
        with open(stylesheet_path, 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        # Crear layout principal
        layout = QtWidgets.QVBoxLayout()

        # Etiqueta "Seleccione una opción"
        label_opcion = QtWidgets.QLabel("Seleccione un Metodo")
        label_opcion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label_opcion.setObjectName("label_opcion")
        layout.addWidget(label_opcion)

        # Crear QGroupBox
        group_box = QtWidgets.QGroupBox()

        # Layout interno del QGroupBox
        layout_box = QtWidgets.QVBoxLayout()

        # Grupo de radio buttons
        self.grupo_opciones = QtWidgets.QButtonGroup()

        # Opciones (radio buttons)
        self.opcion_1 = QtWidgets.QRadioButton("Metodo Biseccion")
        self.opcion_2 = QtWidgets.QRadioButton("Metodo Secante")
        self.opcion_3 = QtWidgets.QRadioButton("Metodo Gauss-Jordan")
        self.opcion_4 = QtWidgets.QRadioButton("Metodo Gauss-Seidel")
        self.opcion_5 = QtWidgets.QRadioButton("Regresion Cuadratica")
        self.opcion_6 = QtWidgets.QRadioButton("Interpolacion Lineal")
        self.opcion_7 = QtWidgets.QRadioButton("Interpolacion Diferencias Divididas")

        # Agregar opciones al grupo
        self.grupo_opciones.addButton(self.opcion_1)
        self.grupo_opciones.addButton(self.opcion_2)
        self.grupo_opciones.addButton(self.opcion_3)
        self.grupo_opciones.addButton(self.opcion_4)
        self.grupo_opciones.addButton(self.opcion_5)
        self.grupo_opciones.addButton(self.opcion_6)
        self.grupo_opciones.addButton(self.opcion_7)

        # Agregar opciones al layout interno
        layout_box.addWidget(self.opcion_1)
        layout_box.addWidget(self.opcion_2)
        layout_box.addWidget(self.opcion_3)
        layout_box.addWidget(self.opcion_4)
        layout_box.addWidget(self.opcion_5)
        layout_box.addWidget(self.opcion_6)
        layout_box.addWidget(self.opcion_7)
        layout_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_box.setSpacing(30)

        # Asignar layout al QGroupBox
        group_box.setLayout(layout_box)

        # Agregar QGroupBox al layout principal
        layout.addWidget(group_box)

        # Botón "Continuar"
        self.button_siguiente = QtWidgets.QPushButton("Continuar")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_siguiente)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_layout)

        # Widget central
        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("MenuWindow")
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.move_window_to_center()

    def move_window_to_center(self):
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindowMenu()
    ventana.show()
    sys.exit(app.exec())
