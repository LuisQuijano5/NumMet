import sys
from PySide6 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()