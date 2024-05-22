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
        self.setWindowTitle('Regresion Cuadratica')
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
        label_opcion = QtWidgets.QLabel("Regresion Cuadratica")
        self.button_a = QtWidgets.QPushButton("?")
        label_false = QtWidgets.QLabel("")
        layout_method_help.addWidget(label_false, alignment=QtCore.Qt.AlignLeft)
        layout_method_help.addWidget(label_opcion, alignment=QtCore.Qt.AlignCenter)
        layout_method_help.addWidget(self.button_a, alignment=QtCore.Qt.AlignRight)

        layout.addLayout(layout_method_help)

        # Textfield para ingresar el tamaño de renglones de la tabla
        layout_renglones = QtWidgets.QHBoxLayout()
        label_renglones = QtWidgets.QLabel("No. de Renglones:")
        layout_renglones.addWidget(label_renglones)
        self.edit_renglones = QtWidgets.QLineEdit()
        int_validator = QtGui.QIntValidator(1, 1000, self)
        self.edit_renglones.setValidator(int_validator)
        layout_renglones.addWidget(self.edit_renglones)

        # Botón para generar renglones
        self.button_generar = QtWidgets.QPushButton("Generar")
        layout_renglones.addWidget(self.button_generar)

        layout.addLayout(layout_renglones)

        # Tabla con dos columnas "X" y "Y"
        self.tabla_datos = QtWidgets.QTableWidget()
        self.tabla_datos.setColumnCount(2)
        self.tabla_datos.setHorizontalHeaderLabels(["X", "Y"])
        self.tabla_datos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        layout.addWidget(self.tabla_datos)

        # Botón Calcular
        self.button_calcular = QtWidgets.QPushButton('Calcular')
        button_calcular_layout = QtWidgets.QHBoxLayout()
        button_calcular_layout.addWidget(self.button_calcular)
        button_calcular_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_calcular_layout)

        # Layout para Resultado y Coeficiente de Correlación
        layout_resultados = QtWidgets.QHBoxLayout()
        # Textfield para Resultado y=
        label_resultado = QtWidgets.QLabel("Resultado y=")
        layout_resultados.addWidget(label_resultado)
        self.edit_resultado = QtWidgets.QLineEdit()
        self.edit_resultado.setReadOnly(True)
        layout_resultados.addWidget(self.edit_resultado)
        # Textfield para Coeficiente de Correlación
        label_coef = QtWidgets.QLabel("Coeficiente de Correlación:")
        layout_resultados.addWidget(label_coef)
        self.edit_coef = QtWidgets.QLineEdit()
        self.edit_coef.setReadOnly(True)
        layout_resultados.addWidget(self.edit_coef)
        layout.addLayout(layout_resultados)

        # Botones "Menú" y "Graficar"
        self.button_menu = QtWidgets.QPushButton('Menú')
        self.button_graficar = QtWidgets.QPushButton('Graficar')
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_menu)
        button_layout.addWidget(self.button_graficar)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_layout)

        # Widget central
        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("Biseccion")
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_error_message(self, error_message):
        QtWidgets.QMessageBox.critical(self, "Error", error_message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
