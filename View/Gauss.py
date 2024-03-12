from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import sys

from PySide6.QtWidgets import QStackedLayout, QWidget, QPushButton


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

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
        body.addWidget(self.buildMain())
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
        spin_noeq = QtWidgets.QSpinBox()
        spin_noeq.setRange(2, 50)

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

    def buildMain(self):
        num_rows = 5
        num_cols = 3

        layout = QtWidgets.QGridLayout()
        layout.setHorizontalSpacing(2)
        layout.setVerticalSpacing(2)

        for row in range(num_rows):
            for col in range(num_cols):
                label = QtWidgets.QLabel(f"x {col + 1}")
                label.setStyleSheet("font-size: 15px; font-weight: bold")
                spin_box = QtWidgets.QSpinBox()
                spin_box.setMinimum(-1000)
                spin_box.setFixedSize(60, 24)

                container = QtWidgets.QWidget()
                hbox = QtWidgets.QHBoxLayout()

                # Add label and spin box to the grid layout
                hbox.addWidget(spin_box)
                hbox.addWidget(label)
                container.setLayout(hbox)

                layout.addWidget(container, row, col * 2)

            equals_label = QtWidgets.QLabel("=")
            equals_label.setStyleSheet("font-size: 15px; font-weight: bold")
            extra_spin_box = QtWidgets.QSpinBox()
            extra_spin_box.setFixedSize(60, 24)
            layout.addWidget(equals_label, row, num_cols * 2)
            layout.addWidget(extra_spin_box, row, num_cols * 2 + 1)

        container = QWidget()
        container.setObjectName('container_main')
        container.setLayout(layout)
        return container

    def buildMatrixOptions(self):
        pass

    def buildResults(self):
        pass

    def buildResultsOptions(self):
        pass

def setAppStyles():
    app.setStyleSheet("* {"
                      "font: 10px 'Helvetica'; } "
                      "#title_label { font-size: 25px; font-weight: 700; }"
                      "QPushButton { "
                      "background-color: black; "
                      "border-radius: 10px;"
                      "color: white;"
                      "font-size: 15px;"
                      "font-weight: 700; }"
                      "#container_top { "
                      "background-color: #DDDDDD; }"
                      "QPushButton:hover { background-color: #777777;}" )

def main():
    setAppStyles()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main()