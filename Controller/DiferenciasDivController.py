import sys
from PySide6 import QtWidgets, QtGui
from View.InterpolacionDifDivNewtonView import MainWindow  # Ajusta la importación según tu estructura de proyecto


class InterpolacionDiferenciasDivididasController:
    def __init__(self, app):
        self.app = app
        self.ventana = MainWindow()
        self.ventana.show()

        # Conectar eventos de la interfaz gráfica a la lógica
        self.ventana.button_generar.clicked.connect(self.generar_renglones)
        self.ventana.button_calcular.clicked.connect(self.calcular)
        self.ventana.button_menu.clicked.connect(self.return_to_menu)
        self.ventana.button_a.clicked.connect(self.help)

        self.move_window_to_center()

    def generar_renglones(self):
        try:
            num_renglones = int(self.ventana.edit_renglones.text())
            self.ventana.tabla_datos.setRowCount(num_renglones)
            # Establecer el validador para asegurarse de que solo se puedan ingresar números dobles en la tabla
            double_validator = QtGui.QDoubleValidator()
            for row in range(num_renglones):
                for col in range(2):
                    editor = self.create_double_editor(double_validator)
                    self.ventana.tabla_datos.setCellWidget(row, col, editor)
        except ValueError:
            self.ventana.show_error_message("Por favor, ingrese un número válido de renglones.")

    def create_double_editor(self, validator):
        editor = QtWidgets.QLineEdit()
        editor.setValidator(validator)
        return editor

    def calcular(self):
        # Aquí iría la lógica de cálculo de la regresión cuadrática
        pass

    def return_to_menu(self):
        # Lógica para volver al menú principal
        from MainController import MainController
        self.main_controller = MainController()
        self.main_controller.show_menu()
        self.ventana.close()

    def help(self):
        # Método para mostrar la ayuda
        QtWidgets.QMessageBox.information(self.ventana, "Ayuda", "Aquí puedes poner la ayuda para el usuario.")

    def move_window_to_center(self):
        # Mover la ventana al centro de la pantalla
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.ventana.width()) / 2
        y = (screen_geometry.height() - self.ventana.height()) / 2
        self.ventana.move(x, y)

    def run(self):
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = InterpolacionDiferenciasDivididasController(app)
    controller.run()
