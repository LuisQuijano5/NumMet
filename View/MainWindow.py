import sys
from PySide6 import QtWidgets
from PySide6   import QtCore
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__ (self):
        super().__init__()
        self.setWindowTitle("METODOS NUMERICOS")
        self.setGeometry(100, 100, 800, 600)

        # Cargar los estilos CSS
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, 'styleSheet.css')
        with open(stylesheet_path, 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        layout = QtWidgets.QVBoxLayout()

        label_app_name = QtWidgets.QLabel("METODOS NUMERICOS")
        label_app_name.setAlignment(QtCore.Qt.AlignCenter)
        label_app_name.setObjectName("label_app_name")
        layout.addWidget(label_app_name)

        creators = ["Creado por:","Jorge Laurencio Sanchez Rojas", "Emiliano Rebolledo Navarrete", "Luis Angel Quijano Guerrero", "Ulises Andrade Gonzalez", "Erick Martín Morin López"]
        for creator in creators:
            label_creator = QtWidgets.QLabel(creator)
            layout.addWidget(label_creator)
            label_creator.setAlignment(QtCore.Qt.AlignCenter)
            label_creator.setObjectName("label_creator")

        self.button_siguiente = QtWidgets.QPushButton("Siguiente")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_siguiente)
        button_layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addLayout(button_layout)



        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("Window")
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
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())