import sys
from PySide6 import QtWidgets
from PySide6 import QtCore
import os
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Método Secante")
        self.setGeometry(100, 100, 800, 600)

        # Cargar los estilos CSS
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, 'styleSheet.css')
        with open(stylesheet_path, 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        # Crear layout principal
        layout = QtWidgets.QVBoxLayout()

        # Label de Metodo
        label_opcion = QtWidgets.QLabel("Metodo Secante")
        label_opcion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_opcion)

        # Layout para ecuacion y boton de Ayuda
        layout_ecuacion = QtWidgets.QHBoxLayout()
        # Textfield para ecuacion
        label_funicon = QtWidgets.QLabel("Funcion")
        layout_ecuacion.addWidget(label_funicon)
        self.edit_ecuacion = QtWidgets.QLineEdit()
        self.edit_ecuacion.setPlaceholderText("De click en el boton de Ayuda (Derecha) para saber como ingresar la funcion")
        layout_ecuacion.addWidget(self.edit_ecuacion)
        # Boton Ayuda
        self.button_a = QtWidgets.QPushButton("?")
        layout_ecuacion.addWidget(self.button_a)

        layout.addLayout(layout_ecuacion)

        # Layout para valores iniciales
        layout_valores = QtWidgets.QHBoxLayout()
        # Label "Valores Iniciales"
        label_valores_iniciales = QtWidgets.QLabel("Valores Iniciales")
        layout_valores.addWidget(label_valores_iniciales)
        # Textfield para a
        self.edit_a = QtWidgets.QLineEdit()
        self.edit_a.setPlaceholderText("Xi-1")
        layout_valores.addWidget(self.edit_a)
        # Textfield para b
        self.edit_b = QtWidgets.QLineEdit()
        self.edit_b.setPlaceholderText("Xi")
        layout_valores.addWidget(self.edit_b)

        layout.addLayout(layout_valores)

        # Layout para Error
        layout_error = QtWidgets.QHBoxLayout()
        # Label "Error"
        label_error = QtWidgets.QLabel("Error")
        layout_error.addWidget(label_error)
        # Textfield para error
        self.edit_error = QtWidgets.QLineEdit()
        self.edit_error.setPlaceholderText('Tolerancia de error')
        layout_error.addWidget(self.edit_error)

        layout.addLayout(layout_error)

        # Boton Calcular
        self.button_calcular = QtWidgets.QPushButton('Calcular')
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_calcular)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(button_layout)

        # Layout para Resultado
        layout_resultado = QtWidgets.QHBoxLayout()
        # Label "Resultado x="
        label_resultado = QtWidgets.QLabel('Resultado x=')
        layout_resultado.addWidget(label_resultado)
        # Textfield para resultado
        self.edit_resultado = QtWidgets.QLineEdit()
        self.edit_resultado.setReadOnly(True)
        layout_resultado.addWidget(self.edit_resultado)

        layout.addLayout(layout_resultado)

        # Tabla de Resultados
        # Crear tabla
        self.tabla_resultados = QtWidgets.QTableWidget()
        self.tabla_resultados.setColumnCount(6)
        self.tabla_resultados.setHorizontalHeaderLabels(["Xi-1", "Xi", "f(Xi-1)", "f(Xi)", "Xi+1", "Error"])

        layout.addWidget(self.tabla_resultados)

        # Botón "Continuar" y "Graficar"
        self.button_graficar = QtWidgets.QPushButton("Graficar")
        self.button_volverMenu = QtWidgets.QPushButton("Menu")
        # Layout para botones volver al Menu y Graficar
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_volverMenu)
        button_layout.addWidget(self.button_graficar)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(button_layout)

        # Widget central
        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("SecantView")
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_error_message(self, error_message):
        QtWidgets.QMessageBox.critical(self, "Error", error_message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())