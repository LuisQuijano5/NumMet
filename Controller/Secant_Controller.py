import sys
from PySide6 import QtWidgets
from View.SecantView import MainWindow
from Model.SecantMethod import SecantSolver

class SecantController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ventana = MainWindow()
        self.ventana.show()

        # Conectar eventos de la interfaz gráfica a la lógica
        self.ventana.button_calcular.clicked.connect(self.calcular)

    def calcular(self):
        expression_function = self.ventana.edit_ecuacion.text()
        error = float(self.ventana.edit_error.text())
        xi_minus_1 = float(self.ventana.edit_a.text())
        xi = float(self.ventana.edit_b.text())

        # Instancia de lógica
        solver = SecantSolver()
        solver.init(expression_function, error, xi_minus_1, xi)
        result = solver.solve()

        # Mostrar resultados
        self.ventana.edit_resultado.setText(result)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    controller = SecantController()
    controller.run()
