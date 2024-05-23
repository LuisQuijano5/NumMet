import sys
from PySide6 import QtWidgets, QtGui
from PySide6 import QtCore
import os

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
stylesheet_path = os.path.join(current_dir, 'styleSheet.css')


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Interpolacion Lineal')
        self.setGeometry(100, 100, 800, 600)

        # Cargar los estilos CSS
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, 'styleSheet.css')
        with open(stylesheet_path, 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        # Crear layout principal
        layout = QtWidgets.QVBoxLayout()

        # Layout para el label de método y el botón de ayuda
        layout_method_help = QtWidgets.QHBoxLayout()
        # Label de Metodo
        label_opcion = QtWidgets.QLabel("Interpolacion Lineal")
        # Boton Ayuda
        self.button_a = QtWidgets.QPushButton("?")

        label_false = QtWidgets.QLabel("")
        layout_method_help.addWidget(label_false, alignment=QtCore.Qt.AlignLeft)
        layout_method_help.addWidget(label_opcion, alignment=QtCore.Qt.AlignCenter)
        layout_method_help.addWidget(self.button_a, alignment=QtCore.Qt.AlignRight)

        layout.addLayout(layout_method_help)

        # Agregar un espaciador vertical
        layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))


        # Layout para x y fx
        layout_fx = QtWidgets.QHBoxLayout()
        # Textfield para ecuacion
        label_x = QtWidgets.QLabel("x")
        layout_fx.addWidget(label_x)
        self.edit_x_IL = QtWidgets.QLineEdit()
        self.edit_x_IL.setPlaceholderText("Ingresa x")
        double_validator = QtGui.QDoubleValidator()
        self.edit_x_IL.setValidator(double_validator)
        layout_fx.addWidget(self.edit_x_IL)
        label_fx = QtWidgets.QLabel("f(x)")
        layout_fx.addWidget(label_fx)
        self.edit_fx_IL = QtWidgets.QLineEdit()
        self.edit_fx_IL.setPlaceholderText("Ingresa f(x)")
        double_validator = QtGui.QDoubleValidator()
        self.edit_fx_IL.setValidator(double_validator)
        layout_fx.addWidget(self.edit_fx_IL)


        layout.addLayout(layout_fx)

        # Agregar un espaciador vertical
        layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Layout para x_0 y f(x_0)
        layout_fx_0 = QtWidgets.QHBoxLayout()
        # Label "Valores Iniciales"
        label_x0_IL = QtWidgets.QLabel("x_0")
        layout_fx_0.addWidget(label_x0_IL)
        self.edit_x0_IL = QtWidgets.QLineEdit()
        self.edit_x0_IL.setPlaceholderText("Ingrese x_0")
        double_validator = QtGui.QDoubleValidator()
        self.edit_x0_IL.setValidator(double_validator)
        layout_fx_0.addWidget(self.edit_x0_IL)
        label_fx0_IL = QtWidgets.QLabel("f(x_0)")
        layout_fx_0.addWidget(label_fx0_IL)
        self.edit_fx0_IL = QtWidgets.QLineEdit()
        self.edit_fx0_IL.setPlaceholderText("Ingrese f(x_0)")
        double_validator = QtGui.QDoubleValidator()
        self.edit_fx0_IL.setValidator(double_validator)
        layout_fx_0.addWidget(self.edit_fx0_IL)

        layout.addLayout(layout_fx_0)

        # Agregar un espaciador vertical
        layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Layout para x_1 y f(x_1)
        layout_fx_1 = QtWidgets.QHBoxLayout()
        # Label "Valores Iniciales"
        label_x1_IL = QtWidgets.QLabel("x_1")
        layout_fx_1.addWidget(label_x1_IL)
        self.edit_x1_IL = QtWidgets.QLineEdit()
        self.edit_x1_IL.setPlaceholderText("Ingrese x_1")
        double_validator = QtGui.QDoubleValidator()
        self.edit_x1_IL.setValidator(double_validator)
        layout_fx_1.addWidget(self.edit_x1_IL)
        label_fx1_IL = QtWidgets.QLabel("f(x_1)")
        layout_fx_1.addWidget(label_fx1_IL)
        self.edit_fx1_IL = QtWidgets.QLineEdit()
        self.edit_fx1_IL.setPlaceholderText("Ingrese f(x_1)")
        double_validator = QtGui.QDoubleValidator()
        self.edit_fx1_IL.setValidator(double_validator)
        layout_fx_1.addWidget(self.edit_fx1_IL)

        layout.addLayout(layout_fx_1)

        # Agregar un espaciador vertical
        layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Boton Calcular
        self.button_calcular = QtWidgets.QPushButton('Calcular')
        self.button_limpiar = QtWidgets.QPushButton('Limpiar')
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_calcular)
        button_layout.addWidget(self.button_limpiar)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(button_layout)

        # Agregar un espaciador vertical
        layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Layout para Error
        layout_error_resultado = QtWidgets.QHBoxLayout()
        # Label "Resultado"
        label_resultado = QtWidgets.QLabel('Resultado ')
        layout_error_resultado.addWidget(label_resultado)
        self.edit_resultado = QtWidgets.QLineEdit()
        self.edit_resultado.setReadOnly(True)
        layout_error_resultado.addWidget(self.edit_resultado)

        label_error = QtWidgets.QLabel("Error")
        layout_error_resultado.addWidget(label_error)
        self.edit_error = QtWidgets.QLineEdit()
        self.edit_error.setReadOnly(True)
        layout_error_resultado.addWidget(self.edit_error)

        layout.addLayout(layout_error_resultado)

        # Agregar un espaciador vertical
        layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Botón "Menu"
        self.button_volverMenu = QtWidgets.QPushButton("Menu")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_volverMenu)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(button_layout)

        # Widget central
        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("Biseccion")
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Conectar botón limpiar con su funcionalidad
        self.button_limpiar.clicked.connect(self.limpiar_campos)

    def limpiar_campos(self):
        # Limpiar todos los campos de entrada y resultados
        self.edit_x_IL.clear()
        self.edit_fx_IL.clear()
        self.edit_x0_IL.clear()
        self.edit_fx0_IL.clear()
        self.edit_x1_IL.clear()
        self.edit_fx1_IL.clear()
        self.edit_resultado.clear()
        self.edit_error.clear()

    def show_error_message(self, error_message):
        QtWidgets.QMessageBox.critical(self, "Error", error_message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
