import os

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import sys

from PySide6.QtWidgets import QStackedLayout, QWidget, QPushButton, QSpinBox, QMessageBox, QScrollArea


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, title, controller):
        super().__init__()
        self.title = title
        self.controller = controller
        self.setupUi()

        # Cargar los estilos CSS
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, 'styleSheet.css')
        with open(stylesheet_path, 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        central_widget = QWidget()
        central_widget.setContentsMargins(0, 0, 0, 0)
        central_widget.setObjectName("GaussWidget")
        #central_widget.setGeometry(300, 300, 600, 600)
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)


    def setupUi(self):
        #self.setAppStyles()
        self.stacked_layout = QStackedLayout()
        self.bodyView = QWidget()
        body = QtWidgets.QVBoxLayout()

        body.addWidget(self.buildTop())
        body.addWidget(self.buildNo())

        self.tableLayout = QStackedLayout()
        self.tableLayout.addWidget(self.buildMain(2, 2))
        tablecontainer = QWidget()
        tablecontainer.setLayout(self.tableLayout)
        body.addWidget(tablecontainer)

        body.addWidget(self.buildTableOptions())

        self.bodyView.setLayout(body)
        self.stacked_layout.addWidget(self.bodyView)

    def buildTop(self):
        title_label = QtWidgets.QLabel()
        title_label.setText(self.title)
        title_label.setObjectName('title_label')

        help_button = QtWidgets.QPushButton(' ? ')
        return_button = QtWidgets.QPushButton(' Menu ')
        """
        rebo adicione los metodos estos para que erick trabaje
        asegurate de ponerlo en tu controlador despues del init para
        que trabaje mas facil erick
        """
        help_button.pressed.connect(self.controller.help)
        return_button.pressed.connect(self.controller.return_to_menu)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(return_button, alignment=Qt.AlignLeft)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        layout.addWidget(help_button, alignment=Qt.AlignRight)

        container = QWidget()
        container.setObjectName('container_top')
        container.setLayout(layout)
        return container

    def buildNo(self):
        label_novar = QtWidgets.QLabel('Numero de Variables')
        #label_noeq = QtWidgets.QLabel('Number of equations')

        self.spin_novar = QtWidgets.QSpinBox()
        self.spin_novar.setRange(2, 26)
        self.spin_novar.setFixedSize(80, 32)
        #self.spin_noeq = QtWidgets.QSpinBox()
        #self.spin_noeq.setRange(2, self.spin_novar.value())
        #self.spin_noeq.setFixedSize(80, 32)

        self.spin_novar.valueChanged.connect(lambda value: self.controller.updateCols(value))
        #self.spin_noeq.valueChanged.connect(lambda value: self.controller.updateRows(value))

        vbox_novar = QtWidgets.QVBoxLayout()
        vbox_novar.addWidget(label_novar)
        vbox_novar.addWidget(self.spin_novar)
        container_novar = QtWidgets.QWidget()
        container_novar.setLayout(vbox_novar)

        #vbox_noeq = QtWidgets.QVBoxLayout()
        #vbox_noeq.addWidget(label_noeq)
        #vbox_noeq.addWidget(self.spin_noeq)
        #container_noeq = QtWidgets.QWidget()
        #container_noeq.setLayout(vbox_noeq)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(container_novar)
        #layout.addWidget(container_noeq)

        container = QWidget()
        container.setObjectName('container_center')
        container.setLayout(layout)
        return container

    def buildMain(self, num_rows, num_cols):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        layout = QtWidgets.QGridLayout()
        layout.setHorizontalSpacing(2)
        layout.setVerticalSpacing(2)

        for row in range(num_rows):
            spin_aux = []
            for col in range(num_cols):
                label = QtWidgets.QLabel(f"x{col + 1}")
                label.setStyleSheet("font-size: 15px; font-weight: bold")
                spin_box = QtWidgets.QDoubleSpinBox()
                spin_box.setMinimum(-1000)
                spin_box.setMaximum(1000)
                spin_box.setFixedSize(112, 36)
                spin_box.setDecimals(3)
                spin_box.setStyleSheet("QDoubleSpinBox { font-size: 16px; }")
                spin_aux.append(spin_box)

                container = QtWidgets.QWidget()
                hbox = QtWidgets.QHBoxLayout()

                hbox.addWidget(spin_box)
                hbox.addWidget(label)
                container.setLayout(hbox)

                layout.addWidget(container, row, col * 2)

            equals_label = QtWidgets.QLabel("=")
            equals_label.setStyleSheet("font-size: 15px; font-weight: bold")
            extra_spin_box = QtWidgets.QDoubleSpinBox()
            extra_spin_box.setMinimum(-1000)
            extra_spin_box.setMaximum(1000)
            extra_spin_box.setFixedSize(112, 36)
            extra_spin_box.setDecimals(3)
            extra_spin_box.setStyleSheet("QDoubleSpinBox { font-size: 16px; }")
            spin_aux.append(extra_spin_box)
            layout.addWidget(equals_label, row, num_cols * 2)
            layout.addWidget(extra_spin_box, row, num_cols * 2 + 1)
            self.controller.spin_matrix.append(spin_aux)

        container = QWidget()
        container.setObjectName("container_main")
        container.setLayout(layout)
        scroll_area.setWidget(container)
        #scroll_area.setGeometry(100, 100, 800, 800)

        return scroll_area

    def buildTableOptions(self):
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        clean_button = QtWidgets.QPushButton("Limpiar")
        solve_button = QtWidgets.QPushButton("Calcular")
        clean_button.pressed.connect(self.controller.cleantable)
        solve_button.pressed.connect(self.controller.solve)

        layout.addWidget(clean_button)
        layout.addWidget(solve_button)

        container = QWidget()
        container.setObjectName('container_matrix_options')
        container.setLayout(layout)
        return container

    def warning(self, message):
        popup = QMessageBox()
        popup.setText(message)
        popup.setWindowTitle("Warning")
        popup.exec()




