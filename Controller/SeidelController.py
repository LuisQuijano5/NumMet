import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton, QScrollArea, QHBoxLayout

from Model.GaussSeidelModel import gauss_seidel
from View.SeidelView import MainWindow

class MatrixWidget(QWidget):
    def __init__(self, matrix):
        super().__init__()
        layout = QVBoxLayout()
        #layout.setSpacing(50)
        for row in matrix:
            row_layout = QHBoxLayout()
            row_layout.setSpacing(25)
            for entry in row:
                label = QLabel(str(entry))
                label.setStyleSheet("QLabel {font-weight: bold; font-size: 15px;}")
                label.setMinimumSize(15, 15)
                row_layout.addWidget(label)
            layout.addLayout(row_layout)
        self.setLayout(layout)

class SeidelController:

    def __init__(self):
        self.matrix_widgets = []
        self.rows = 2
        self.cols = 2
        self.spin_matrix = []
        #rebo: conecta asi tu view en tu controller, mandale el titulo y self
        self.app = QtWidgets.QApplication(sys.argv)
        self.view = MainWindow("Gauss Seidel", self)
        self.setAppStyles()

        self.view.resize(800, 600)

        self.scroll_area = QScrollArea()  # Create a QScrollArea
        self.scroll_area.setWidgetResizable(True)  # Allow scrolling

        self.results_container = QWidget()
        self.results_view = QVBoxLayout()
        self.results_view.setAlignment(Qt.AlignCenter)
        return_button = QPushButton("Return")
        return_button.clicked.connect(self.goMain)
        self.results_view.addWidget(return_button)
        self.results_container.setLayout(self.results_view)

        self.scroll_area.setWidget(self.results_container)  # Set widget to scroll area
        self.view.stacked_layout.addWidget(self.scroll_area)

        self.view.show()
        sys.exit(self.app.exec())

    def help(self):
        print("hola erick aqui lo del manual :)")

    def return_to_menu(self):
        print("hola erick aqui cierras esta venta y que se abra menu")

    def updateCols(self, cols):
        if self.cols != cols and cols >= 2 and cols < 100:
            self.cols = int(cols)
            self.rows = int(cols)
                # self.view.spin_noeq.setRange(2, cols)
            self.rebuild()

    def updateEp(self,eP):
        self.ep=eP

    def rebuild(self):
        self.spin_matrix = []
        while self.view.tableLayout.count() > 0:
            self.view.tableLayout.takeAt(0).widget().deleteLater()

        self.view.tableLayout.addWidget(self.view.buildMain(self.rows, self.cols))

    def cleantable(self):
        for i in self.spin_matrix:
            for j in i:
                j.setValue(0)

    def check_row(self, row):
        for i in row:
            if i != 0: return True
        self.view.warning("Please enter at least one value diff from zero in each equation.\n"
                          "The table will be restored")
        self.rebuild()
        return False

    def setAppStyles(self):
        self.app.setStyleSheet("* {"
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
                          "QPushButton:hover { background-color: #777777;}")


    """
    UNIQUE TO GAUSS JORDAN
    """

    def solve(self):
        self.matrix = []
        for i in self.spin_matrix:
            aux = []
            for j in i:
                aux.append(j.value())
            if (not self.check_row(aux)): return
            self.matrix.append(aux)

        for i in self.matrix:
            print(i)

        print(self.matrix)

        try:
            historial, solX = gauss_seidel(self.matrix, self.ep)
        except:
            self.view.warning("Revisa que el sistema este completo y asegurese de ingresar un error permitido")
            return
        # print("Solution:", solution)
        # print("State after each iteration:")
        # for i, matrix in enumerate(state):
        #   print(f"Iteration {i+1}:")
        #   for row in matrix:
        #       print(row)

        self.createResults(historial, solX)

    def createResults(self, historial, solX):
        self.updateResults(solX, historial)
        print(historial)
        self.view.stacked_layout.setCurrentIndex(1)

    def goMain(self):
        self.view.stacked_layout.setCurrentIndex(0)

    def updateResults(self, solX, historial):
        #clear view

        for matrix_widget in self.matrix_widgets:
            matrix_widget.setParent(None)


        # Create and add new matrix widgets
        #for matrix in list:
         #   matrix_widget = MatrixWidget(matrix)
          #  self.results_view.addWidget(matrix_widget)
           # self.matrix_widgets.append(matrix_widget)
        layout_his=QVBoxLayout()
        his_cont=QWidget()

        html_his=f"<pre>{historial}</pre>"

        labelHis=QLabel()
        labelHis.setText(html_his)

        layout_his.addWidget(labelHis)
        his_cont.setLayout(layout_his)
        his_cont.setGeometry(100,100,400,200)

        self.results_view.addWidget(his_cont)

        x_values = QHBoxLayout()
        x_values.setSpacing(15)
        x_values_container = QWidget()
        x_values_container.setStyleSheet("background-color: #dddddd")
        if(solX==0):
            label=QLabel('El sistema no converge')
            label.setStyleSheet("QLabel {font-weight: bold; font-size: 15px;}")
            x_values.addWidget(label)
        else:
            for i, x in enumerate(solX):
                label = QLabel(f"x{i + 1}: " + str(x))
                label.setStyleSheet("QLabel {font-weight: bold; font-size: 15px;}")
                x_values.addWidget(label)
        x_values_container.setLayout(x_values)
        self.matrix_widgets.append(x_values_container)
        self.results_view.addWidget(x_values_container)


def main():
    SeidelController()

if __name__ == "__main__":
    main()
