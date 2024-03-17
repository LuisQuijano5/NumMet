from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import sys

from PySide6.QtWidgets import QStackedLayout, QWidget, QPushButton, QSpinBox, QMessageBox
import Controller.GaussJordan_Controller as controller
with open('styleSheet.css', 'r') as f:
    stylesheet = f.read()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.gaussjordan = controller.GaussJordanController(self)
        self.setupUi()
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        central_widget.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

    def setupUi(self):
        self.stacked_layout = QStackedLayout()
        view = QWidget()
        body = QtWidgets.QVBoxLayout()

        body.addWidget(self.buildTop())
        body.addWidget(self.buildNo())

        self.tableLayout = QStackedLayout()
        self.tableLayout.addWidget(self.buildMain(2, 2))
        tablecontainer = QWidget()
        tablecontainer.setLayout(self.tableLayout)
        body.addWidget(tablecontainer)

        body.addWidget(self.buildTableOptions())

        view.setLayout(body)
        self.stacked_layout.addWidget(view)

    def buildTop(self):
        title_label = QtWidgets.QLabel()
        title_label.setText('Gauss-Jordan')
        title_label.setObjectName('title_label')

        help_button = QtWidgets.QPushButton(' ? ')
        return_button = QtWidgets.QPushButton(' Return ')

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(return_button, alignment=Qt.AlignLeft)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        layout.addWidget(help_button, alignment=Qt.AlignRight)

        container = QWidget()
        container.setObjectName('container_top')
        container.setLayout(layout)
        return container

    def buildNo(self):
        label_novar = QtWidgets.QLabel('Number of variables')
        label_noeq = QtWidgets.QLabel('Number of equations')

        spin_novar = QtWidgets.QSpinBox()
        spin_novar.setRange(2, 50)
        spin_novar.setFixedSize(80, 32)

        spin_noeq = QtWidgets.QSpinBox()
        spin_noeq.setRange(2, 50)
        spin_noeq.setFixedSize(80, 32)

        spin_novar.valueChanged.connect(lambda value: self.gaussjordan.updateCols(value))
        spin_noeq.valueChanged.connect(lambda value: self.gaussjordan.updateRows(value))

        vbox_novar = QtWidgets.QVBoxLayout()
        vbox_novar.addWidget(label_novar)
        vbox_novar.addWidget(spin_novar)
        container_novar = QtWidgets.QWidget()
        container_novar.setLayout(vbox_novar)

        vbox_noeq = QtWidgets.QVBoxLayout()
        vbox_noeq.addWidget(label_noeq)
        vbox_noeq.addWidget(spin_noeq)
        container_noeq = QtWidgets.QWidget()
        container_noeq.setLayout(vbox_noeq)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(container_novar)
        layout.addWidget(container_noeq)

        container = QWidget()
        container.setObjectName('container_center')
        container.setLayout(layout)
        return container

    def buildMain(self, num_rows, num_cols):
        layout = QtWidgets.QGridLayout()
        layout.setHorizontalSpacing(2)
        layout.setVerticalSpacing(2)

        for row in range(num_rows):
            spin_aux = []
            for col in range(num_cols):
                label = QtWidgets.QLabel(f"x {col + 1}")
                label.setStyleSheet("font-size: 15px; font-weight: bold")
                spin_box = QtWidgets.QSpinBox()
                spin_box.setMinimum(-1000)
                spin_box.setFixedSize(60, 24)
                spin_aux.append(spin_box)

                container = QtWidgets.QWidget()
                hbox = QtWidgets.QHBoxLayout()

                hbox.addWidget(spin_box)
                hbox.addWidget(label)
                container.setLayout(hbox)

                layout.addWidget(container, row, col * 2)

            equals_label = QtWidgets.QLabel("=")
            equals_label.setStyleSheet("font-size: 15px; font-weight: bold")
            extra_spin_box = QtWidgets.QSpinBox()
            extra_spin_box.setFixedSize(60, 24)
            spin_aux.append(extra_spin_box)
            layout.addWidget(equals_label, row, num_cols * 2)
            layout.addWidget(extra_spin_box, row, num_cols * 2 + 1)
            self.gaussjordan.spin_matrix.append(spin_aux)

        container = QWidget()
        container.setObjectName('container_main')
        container.setLayout(layout)
        return container

    def buildTableOptions(self):
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        clean_button = QtWidgets.QPushButton("Clean")
        solve_button = QtWidgets.QPushButton("Solve")
        clean_button.pressed.connect(self.gaussjordan.cleantable)
        solve_button.pressed.connect(self.gaussjordan.solve)

        layout.addWidget(clean_button)
        layout.addWidget(solve_button)

        container = QWidget()
        container.setObjectName('container_matrix_options')
        container.setLayout(layout)
        return container

    def buildResults(self):
        pass

    def buildResultsOptions(self):
        pass

    def warning(self, message):
        popup = QMessageBox()
        popup.setText(message)
        popup.setWindowTitle("Warning")
        popup.exec()



def main():
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    main()