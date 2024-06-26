import sys
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QDialog, QScrollArea, QWidget, QVBoxLayout, QLabel

from View.RegresionCuadraticaView import MainWindow
from Model.QuadraticRegression_Method import quadratic_regression


class RegresionCuadraticaController:
    def __init__(self, app):
        self.app = app
        self.ventana = MainWindow()
        self.ventana.show()

        # Conectar eventos de la interfaz gráfica a la lógica
        self.ventana.button_generar.clicked.connect(self.generar_renglones)
        self.ventana.button_calcular.clicked.connect(self.calcular)
        self.ventana.button_menu.clicked.connect(self.return_to_menu)
        self.ventana.button_a.clicked.connect(self.help)
        self.y_values = None
        self.x_values = None

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

        #Lo siguiente es un ejemplo de como mandar los valores a los texfield de resultados
        #realice una operacion para que se pudiera entender mejor
        #(los resultados solo se ven hasta que se da click en el boton de calcular)
        resultado = 1 + 3
        coeficiente_correlacion = 0.85

        # Asignar los resultados a los textfields correspondientes
        self.ventana.edit_resultado.setText(str(resultado))
        self.ventana.edit_coef.setText(str(coeficiente_correlacion))

        # Lo siguiente son ejemplos de manejo de los arreglos de numeros X y Y
        # Obtener los valores de x e y
        x_values, y_values = self.obtener_valores()

        #si con pytho 12 no les jala comenten lo de arriba y usen esto>
        # x_values = [float(i) for i in self.obtener_valores()[0]]
        #
        # y_values = [float(i) for i in self.obtener_valores()[1]]



        # Verificar si hay valores vacíos
        if not x_values or not y_values:
            self.ventana.show_error_message("Por favor, complete todas las casillas de la tabla.")
            return

        """
        HERE
        """
        eq, sr = quadratic_regression(x_values, y_values)
        #lc = LinealRegression()
        #r, ec = lc.iterate(x_values, y_values)

        # Lo siguiente es un ejemplo de como mandar los valores a los texfield de resultados
        # realice una operacion para que se pudiera entender mejor
        # (los resultados solo se ven hasta que se da click en el boton de calcular)
        resultado = eq
        coeficiente_correlacion = sr

        # Asignar los resultados a los textfields correspondientes
        self.ventana.edit_resultado.setText(str(resultado))
        self.ventana.edit_coef.setText(str(coeficiente_correlacion))

        # # Ejemplo de como es el formato de los valores
        # print("Valores de x en calcular:", x_values)
        # print("Valores de y en calcular:", y_values)
        # print("Valor de x_0", x_values[0])
        #
        # # Ejemplo de acceso a valores individuales
        # if x_values and y_values:
        #     for i in range(len(x_values)):
        #         x_val = x_values[i]
        #         y_val = y_values[i]
        #         print(f"Valor de x[{i}]:", x_val)
        #         print(f"Valor de y[{i}]:", y_val)
        #
        # # Aquí puedes agregar lógica adicional que utilice estos valores individuales
        # # Los valores se obtiene hasta que se da click en el boton de calcular, si los ocupan de otra forma me avisan
        # pass


    def obtener_valores(self):
        try:
            self.x_values = []
            self.y_values = []
            num_renglones = self.ventana.tabla_datos.rowCount()

            for row in range(num_renglones):
                x_item = self.ventana.tabla_datos.cellWidget(row, 0)
                y_item = self.ventana.tabla_datos.cellWidget(row, 1)

                if x_item and y_item:
                    x_value = x_item.text()
                    y_value = y_item.text()

                    if x_value and y_value:
                        self.x_values.append(float(x_value))
                        self.y_values.append(float(y_value))
                    else:
                        # Si alguna celda está vacía, mostramos un error y detenemos el proceso
                        self.ventana.show_error_message("Todas las casillas deben estar llenas.")
                        return [], []

            # Imprimir los valores para ver que se están guardando bien
            print("Valores de x:", self.x_values)
            print("Valores de y:", self.y_values)

            return self.x_values, self.y_values
        except Exception as e:
            self.ventana.show_error_message(f"Error al obtener los valores: {str(e)}")
            return [], []

    def return_to_menu(self):
        # Lógica para volver al menú principal
        from MainController import MainController
        self.main_controller = MainController()
        self.main_controller.show_menu()
        self.ventana.close()

    def help(self):
        # Método para mostrar la ayuda
        help_dialog = QDialog()
        help_dialog.setWindowTitle("Manual de Usuario Regresión")
        help_dialog.setFixedSize(800, 500)

        scroll_area = QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        content_widget = QWidget()
        content_layout = QVBoxLayout()

        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Manual de Usuario Regresión cuadrática")
        title_label.setStyleSheet("font-family: Arial, sans-serif; font-size:14pt;;")
        content_layout.addWidget(title_label)

        # Instrucciones
        instructions_label = QLabel(
            """
            Ayuda Regresión Cuadrática, es regresión para exclusivamente m = 2
            El método pide introducir la tabla de valores de x y f(x) o sea y.
            Con estos valores el método encuentra los coeficientes necesarios para generar la ecuación además del coef de correlación.
            
            La primera casilla, número de renglones, es la cantidad de datos o tuplas o registros que se piensan
            introducir, o sea n. Al presionar el botón de generar se actualiza el número de renglones
            ¡Cuidado!, esto borrará los registros que esten en la tabla.
            
            Hay que llenar toda la tabla o el método no te permitira calcular correctamente los datos.
            
            Una vez todo llenado, presiona calcular para ver los valores resultantes que se encuentran en la parte inferior.
            y = a la ecuación, r =  coef correlación.
            
            Puedes cambiar valores si quieres calcular algo más.
            
            Con el botón de menú puedes regresar a seleccionar el método numérico de tu preferencia
            """
        )
        instructions_label.setStyleSheet("font-family: Arial, sans-serif; font-size:11pt;")
        content_layout.addWidget(instructions_label)

        # Botón de regresar
        return_button = QPushButton("Volver")
        return_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;")
        return_button.clicked.connect(help_dialog.close)
        content_layout.addWidget(return_button)
        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area)

        help_dialog.setLayout(layout)
        help_dialog.exec()


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
    controller = RegresionCuadraticaController()
    controller.run()
