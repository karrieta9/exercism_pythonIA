class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")
        
    def row(self, index):
        rows = []
        for i in self.matrix_string[index-1].split(' '):
            rows.append(int(i))
        return rows

    def column(self, index):
        columns = []
        for i in self.matrix_string:
            columns.append(int(i.split(" ")[index - 1]))
        return columns

