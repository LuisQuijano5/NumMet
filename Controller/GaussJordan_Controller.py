from Model.test import gauss_jordan
class GaussJordanController:
    def __init__(self, view):
        self.view = view
        self.rows = 2
        self.cols = 2
        self.spin_matrix = []

    def updateCols(self, cols):
        if self.cols != cols and cols > 2 and cols < 100:
            self.cols = int(cols)
            self.rebuild()

    def updateRows(self, rows):
        if self.rows != rows and rows > 2 and rows < 100:
            self.rows = int(rows)
            self.rebuild()

    def rebuild(self):
        self.spin_matrix = []
        while self.view.tableLayout.count() > 0:
            self.view.tableLayout.takeAt(0).widget().deleteLater()

        self.view.tableLayout.addWidget(self.view.buildMain(self.rows, self.cols))

    def cleantable(self):
        for i in self.spin_matrix:
            for j in i:
                j.setValue(0)

    def solve(self):
        self.matrix = []
        for i in self.spin_matrix:
            aux = []
            for j in i:
                aux.append(int(j.value()))
            if(not self.check_row(aux)): return
            self.matrix.append(aux)

        for i in self.matrix:
            print(i)

        solution, state = gauss_jordan(self.matrix)
        print("Solution:", solution)
        print("State after each iteration:")
        for i, matrix in enumerate(state):
           print(f"Iteration {i+1}:")
           for row in matrix:
               print(row)

    def check_row(self, row):
        for i in row:
            if i != 0: return True
        self.view.warning("Please enter at least one value diff from zero in each equation.\n"
                          "The table will be restored")
        self.rebuild()
        return False

