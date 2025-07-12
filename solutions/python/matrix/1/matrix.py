class Matrix:
    def __init__(self, matrix_string):
        self.matrix=list(map(lambda row: row.split(' '),matrix_string.split('\n')))

    def row(self, index):
        return list(map(int,self.matrix[index - 1]))

    def column(self, index):
        column=[row[index - 1] for row in self.matrix]
        return list(map(int,column))
        
        