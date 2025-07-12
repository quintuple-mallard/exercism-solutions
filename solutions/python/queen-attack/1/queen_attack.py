class Queen:
    def __init__(self, row, column):
        if row <0:
            raise ValueError('row not positive')
        elif row>=8 or row%1!=0:
            raise ValueError('row not on board')
        if column<0:
           raise ValueError("column not positive") 
        elif column>=8 or column%1!=0:
            raise ValueError('column not on board')
        self.row=row
        self.column=column
    def can_attack(self, another_queen):
        if self.row==another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        elif self.row==another_queen.row or self.column == another_queen.column:
            return True
        elif abs(self.row-another_queen.row)==abs(self.column-another_queen.column):
            return True
        return False
