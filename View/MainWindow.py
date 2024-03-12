import sys
from PySide6 import QtWidgets
from PySide6   import QtCore
with open('styleSheet.css', 'r') as f:
    stylesheet = f.read()

class MainWindow(QtWidgets.QMainWindow):

    def __init__ (self):
        super().__init__()
        self.setWindowTitle('Metodos Numericos')
        self.setGeometry(100, 100, 800, 600)

        layout = QtWidgets.QVBoxLayout()

        label_app_name = QtWidgets.QLabel('Metodos Numericos')
        label_app_name.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label_app_name)

        creators = ["CREADO POR:","Jorge Laurencio Sanchez Rojas", "Emiliano Rebolledo Navarrete", "Luis Angel Quijano Guerrero", "Ulises Andrade Gonzalez", "Erick Martín Morin López"]
        for creator in creators:
            label_creator = QtWidgets.QLabel(creator)
            layout.addWidget(label_creator)
            label_creator.setAlignment(QtCore.Qt.AlignCenter)

        button_siguiente = QtWidgets.QPushButton("Siguiente")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(button_siguiente)
        button_layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addLayout(button_layout)

        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("Window")
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())