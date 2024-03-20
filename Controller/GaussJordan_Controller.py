from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton, QScrollArea, QHBoxLayout, QDialog

from Model.test import gauss_jordan
from View.Gauss import MainWindow

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

class GaussJordanController:

    def __init__(self, app):
        self.matrix_widgets = []
        self.rows = 2
        self.cols = 2
        self.spin_matrix = []
        #rebo: conecta asi tu view en tu controller, mandale el titulo y self
        self.app = app
        self.view = MainWindow("Gauss Jordan", self)


        self.view.resize(800, 600)

        self.scroll_area = QScrollArea()  # Create a QScrollArea
        self.scroll_area.setWidgetResizable(True)  # Allow scrolling

        self.results_container = QWidget()
        self.results_view = QVBoxLayout()
        self.results_view.setAlignment(Qt.AlignCenter)
        return_button = QPushButton("Volver el Metodo")
        return_button.clicked.connect(self.goMain)
        self.results_view.addWidget(return_button)
        self.results_container.setLayout(self.results_view)

        self.scroll_area.setWidget(self.results_container)  # Set widget to scroll area
        self.view.stacked_layout.addWidget(self.scroll_area)

        self.view.show()

    def help(self):
        help_dialog = QDialog()
        help_dialog.setWindowTitle("Manual de Usuario Gauss-Jordan")
        help_dialog.setFixedSize(800, 500)

        scroll_area = QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        content_widget = QWidget()
        content_layout = QVBoxLayout()

        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Manual de Usuario Gauss-Jordan")
        title_label.setStyleSheet("font-family: Arial, sans-serif; font-size:14pt;;")
        content_layout.addWidget(title_label)

        # Instrucciones
        instructions_label = QLabel(
            "Funcionamiento:\n"
            "Esta ventana permite solucionar matrices con soluciones únicas, es decir, aquellas en las que hay\n "
            "el mismo número de ecuaciones que de variables y que cada variable aparece por lo menos en una ecuación.\n\n"
            "Puedes modificar la cantidad de variables o ecuaciones usando la casilla 'Number of variables',\n "
            "acepta valores enteros entre 2 a 26 y genera automáticamente la cantidad de casillas necesarias para\n "
            "escribir las matrices.\n\n"
            "El recuadro inicial contiene las 'casillas' para poner los coeficientes de cada variable en cada ecuación,\n "
            "acepta valores de 3 decimales de entre -1000 a 1000. Recuerda llenar el resultado también y usar ',' para \n"
            "los decimales.\n""Para acceder a su llenado se debe dar click en ellos, o en su defecto usar las flechas para \n"
            "aumentar o disminuir en una unidad.\n\n"
            "La tecla Tab puedes moverte de casillas\n\n"
            "El 'botón clean' regresará las casillas de coeficientes a 0.\n\n"
            "El 'botón solve' mostrará otra vista en la misma ventana donde se encontrará el proceso seguido por matrices\n "
            "y el resultado.Para regresar solo presiona el botón return que aparecerá hasta arriba.\n\n"
            "Consideraciones:\n"
            "El programa mostrará 3 decimales en resultados.\n"
            "En caso de ser necesario el programa adicionará barras de desplazamiento para observar el contenido completo.\n"
            "En caso de haber colocado en desorden las ecuaciones, el programa se encargará de ordenarlo para su solución.\n"
            "En caso de no colocar por lo menos en una ecuación una variable el programa te mostrará una advertencia.\n"
            "En caso de dejar una ecuación en ceros, el programa mostrará una advertencia."
        )
        instructions_label.setStyleSheet("font-family: Arial, sans-serif; font-size:11pt;")
        content_layout.addWidget(instructions_label)

        # Botón de regresar
        return_button = QPushButton("Volver")
        return_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;")
        return_button.clicked.connect(help_dialog.close)
        content_layout.addWidget(return_button)
        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area)

        help_dialog.setLayout(layout)
        help_dialog.exec()

    def return_to_menu(self):
        from MainController import MainController
        self.main_controller = MainController()
        self.main_controller.show_menu()
        self.view.close()



    def updateCols(self, cols):
        if self.cols != cols and cols >= 2 and cols < 100:
            self.cols = int(cols)
            self.rows = int(cols)
            #self.view.spin_noeq.setRange(2, cols)
            self.rebuild()

#    def updateRows(self, rows):
#        if self.rows != rows and rows >= 2 and rows < 100:
#            self.rows = int(rows)
#            self.rebuild()

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
        self.view.warning("Por Favor Ingresa al menos un valor diferente de cero en cada ecuacion.\n"
                          "La tabla se limpiara")
        self.rebuild()
        return False


    def solve(self):
        self.matrix = []
        for i in self.spin_matrix:
            aux = []
            for j in i:
                aux.append(j.value())
            if(not self.check_row(aux)): return
            self.matrix.append(aux)

        #for i in self.matrix:
        #    print(i)

        try:
            solution, state = gauss_jordan(self.matrix)
        except:
            self.view.warning("Revisa tus ecuaciones por favor, no ingreses una matriz singular")
            return
        #print("Solution:", solution)
        #print("State after each iteration:")
        #for i, matrix in enumerate(state):
        #   print(f"Iteration {i+1}:")
        #   for row in matrix:
        #       print(row)
        
        self.createResults(solution, state)

    def createResults(self, solution, list):
        self.updateResults(solution, list)
        self.view.stacked_layout.setCurrentIndex(1)

    def goMain(self):
        self.view.stacked_layout.setCurrentIndex(0)

    def updateResults(self, solution, list):
        #clear view
        for matrix_widget in self.matrix_widgets:
            matrix_widget.setParent(None)

        # Create and add new matrix widgets
        for matrix in list:
            matrix_widget = MatrixWidget(matrix)
            self.results_view.addWidget(matrix_widget)
            self.matrix_widgets.append(matrix_widget)

        x_values = QHBoxLayout()
        x_values.setSpacing(15)
        x_values_container = QWidget()
        x_values_container.setStyleSheet("background-color: #dddddd")
        for i, x in enumerate(solution):
            label = QLabel(f"x{i+1}: " + str(x))
            label.setStyleSheet("QLabel {font-weight: bold; font-size: 15px;}")
            x_values.addWidget(label)
        x_values_container.setLayout(x_values)
        self.matrix_widgets.append(x_values_container)
        self.results_view.addWidget(x_values_container)

    def move_window_to_center(self):
        # Mover la ventana al centro de la pantalla
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.view.width()) / 2
        y = (screen_geometry.height() - self.view.height()) / 2
        self.view.move(x, y)
