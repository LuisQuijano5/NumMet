import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from View.SecantView import MainWindow
from Model.SecantMethod import SecantSolver
from Model.Equation_Solver import Function
from PySide6 import QtGui


class SecantController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ventana = MainWindow()
        self.ventana.show()

        # Conectar eventos de la interfaz gráfica a la lógica
        self.ventana.button_calcular.clicked.connect(self.calcular)
        self.ventana.button_graficar.clicked.connect(self.graficar)

    def calcular(self):
        expression_function = self.ventana.edit_ecuacion.text()
        error = float(self.ventana.edit_error.text())
        xi_minus_1 = float(self.ventana.edit_a.text())
        xi = float(self.ventana.edit_b.text())

        # Instancia de lógica
        solver = SecantSolver()
        solver.init(expression_function, error, xi_minus_1, xi)
        solver_results = solver.solve()

        # Limpiar la tabla antes de agregar nuevos resultados
        self.ventana.tabla_resultados.clearContents()
        self.ventana.tabla_resultados.setRowCount(0)

        # Agregar los resultados a la tabla
        for i, (xi_minus_1, xi, f_xi_minus_1, f_xi, xi_plus_1, error) in enumerate(solver_results):
            self.ventana.tabla_resultados.insertRow(i)
            self.ventana.tabla_resultados.setItem(i, 0, QtWidgets.QTableWidgetItem(str(xi_minus_1)))
            self.ventana.tabla_resultados.setItem(i, 1, QtWidgets.QTableWidgetItem(str(xi)))
            self.ventana.tabla_resultados.setItem(i, 2, QtWidgets.QTableWidgetItem(str(f_xi_minus_1)))
            self.ventana.tabla_resultados.setItem(i, 3, QtWidgets.QTableWidgetItem(str(f_xi)))
            self.ventana.tabla_resultados.setItem(i, 4, QtWidgets.QTableWidgetItem(str(xi_plus_1)))
            self.ventana.tabla_resultados.setItem(i, 5, QtWidgets.QTableWidgetItem(str(error)))

        # Mostrar resultados
        self.ventana.edit_resultado.setText(str(solver_results[-1][4]))

    def graficar(self):
        # Método para graficar la función
        expression_function = self.ventana.edit_ecuacion.text()
        function = Function(expression_function)

        # Obtener la ruta de la imagen generada
        ruta_imagen = function.plot()

        # Crear una nueva ventana para mostrar la gráfica
        ventana_grafica = QtWidgets.QMainWindow()
        ventana_grafica.setWindowTitle("Gráfica de la función")

        # Cargar la imagen y obtener sus dimensiones
        pixmap = QPixmap(ruta_imagen)
        ancho_imagen = pixmap.width()
        alto_imagen = pixmap.height()

        # Establecer el tamaño de la ventana según las dimensiones de la imagen
        ventana_grafica.setFixedSize(ancho_imagen, alto_imagen)

        # Crear un widget para mostrar la gráfica
        widget_grafica = QtWidgets.QWidget()
        layout_grafica = QtWidgets.QVBoxLayout()
        widget_grafica.setLayout(layout_grafica)
        ventana_grafica.setCentralWidget(widget_grafica)

        # Mostrar la imagen en la nueva ventana
        label_grafica = QtWidgets.QLabel()
        label_grafica.setPixmap(pixmap)
        layout_grafica.addWidget(label_grafica)

        # Mostrar la nueva ventana
        ventana_grafica.show()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    controller = SecantController()
    controller.run()