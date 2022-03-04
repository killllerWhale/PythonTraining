class Table:

    def __init__(self, row, col):
        self.tableList = [[0] * row for i in range(col)]

    def set_value(self, row, col, value):
        self.tableList[col-1][row-1] = value

    def get_value(self, row, col):
        return self.tableList[col-1][row-1] if (col-1)<self.n_cols() and (row-1)<self.n_rows() else "None"

    def n_cols(self):
        return len(self.tableList)

    def n_rows(self):
        return len(self.tableList[0])


table = Table(3, 5)
# table.set_value(3, 5, 10)
# print(table.get_value(3, 5))
table.set_value(3, 5, 10)
print(table.get_value(3, 6))
# print(table.n_rows())
# print(table.n_cols())
