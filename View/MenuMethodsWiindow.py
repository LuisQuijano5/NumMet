import sys
from PySide6 import QtWidgets
from PySide6 import QtCore
with open('styleSheet.css', 'r') as f:
    stylesheet = f.read()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccione una opción")
        self.setGeometry(100, 100, 800, 600)

        # Crear layout principal
        layout = QtWidgets.QVBoxLayout()

        # Etiqueta "Seleccione una opción"
        label_opcion = QtWidgets.QLabel("Seleccione un Metodo")
        label_opcion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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
        self.opcion_3 = QtWidgets.QRadioButton("Metodo Gauss-Jorda")
        self.opcion_4 = QtWidgets.QRadioButton("Metodo Gauss-Seidel")

        # Agregar opciones al grupo
        self.grupo_opciones.addButton(self.opcion_1)
        self.grupo_opciones.addButton(self.opcion_2)
        self.grupo_opciones.addButton(self.opcion_3)
        self.grupo_opciones.addButton(self.opcion_4)

        # Agregar opciones al layout interno
        layout_box.addWidget(self.opcion_1)
        layout_box.addWidget(self.opcion_2)
        layout_box.addWidget(self.opcion_3)
        layout_box.addWidget(self.opcion_4)
        layout_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_box.setSpacing(30)

        # Asignar layout al QGroupBox
        group_box.setLayout(layout_box)

        # Agregar QGroupBox al layout principal
        layout.addWidget(group_box)

        # Botón "Continuar"
        button_siguiente = QtWidgets.QPushButton("Continuar")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(button_siguiente)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_layout)

        # Widget central
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
