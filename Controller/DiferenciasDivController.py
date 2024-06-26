import sys
from PySide6 import QtWidgets, QtGui
from View.InterpolacionDifDivNewtonView import MainWindow
from Model.InterpolacionDifDivNewtonModel import calcularPunto


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
        self.x_values = None
        self.y_values = None
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

        # Obtener el valor de X ingresado en el campo correspondiente
        valor_x = float(self.ventana.edit_X.text())
        print("Valor de X ingresado:", valor_x)

        # Lo siguiente es un ejemplo de como mandar los valores a los texfield de resultados
        # realice una operacion para que se pudiera entender mejor
        # (los resultados solo se ven hasta que se da click en el boton de calcular)
        resultado = 1 + 3
        # Asignar los resultados a los textfields correspondientes
        self.ventana.edit_resultado.setText(str(resultado))

        # Obtener los valores de x e y
        #x_values, y_values = self.obtener_valores()

        x_values = [float(i) for i in self.obtener_valores()[0]]

        y_values = [float(i) for i in self.obtener_valores()[1]]

        valor_y=calcularPunto(x_values, y_values,valor_x)

        self.ventana.edit_resultado.setText(str(valor_y))

        # Verificar si hay valores vacíos
        if not x_values or not y_values:
            self.ventana.show_error_message("Por favor, complete todas las casillas de la tabla.")
            return

        # Ejemplo de como es el formato de los valores
        print("Valores de x en calcular:", x_values)
        print("Valores de y en calcular:", y_values)
        print("Valor de x_0", x_values[0])
        # Ejemplo de acceso a valores individuales
        if x_values and y_values:
            for i in range(len(x_values)):
                x_val = x_values[i]
                y_val = y_values[i]
                print(f"Valor de x[{i}]:", x_val)
                print(f"Valor de y[{i}]:", y_val)

        # Aquí puedes agregar lógica adicional que utilice estos valores individuales
        # Los valores se obtiene hasta que se da click en el boton de calcular, si los ocupan de otra forma me avisan
        pass

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
        QtWidgets.QMessageBox.information(self.ventana, "Ayuda",
                                          "Primero ingresa el número de puntos que conoces, después ingresa el valor a\n"
                                          "interpolar, da clic en 'Generar' para finalmente ingresar los puntos que "
                                          "se conocen.\n\n"
                                          
                                          "Antes de calcular verifica que no queden casillas vacías y que no cometas alguno de los\n"
                                          "siguientes errores.\n\n"                                          
                                          
                                          "ERRORES NO PERMITIDOS\n\n"
                                          
                                          "-No se debe ingresar el mismo punto dos veces.\n"
                                          "-No se debe ingresar valores repetidos de X aunque los valores de Y sean diferentes.\n"                                          
                                          "-En la lista de puntos conocidos no se debe ingresar el valor de X que se desea calcular.\n"
                                          )

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
    controller = InterpolacionDiferenciasDivididasController()
    controller.run()
