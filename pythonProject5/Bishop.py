class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "B"

    def getColor(self):
        return self.color

    def canMove(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if abs(row - self.row) == abs(col - self.col):
            return True
        return False

BLACK=2
WHITE=1
row0 = 7
col0 = 5
bishopOne = Bishop(row0, col0, BLACK)
print('white' if bishopOne.getColor() == WHITE else 'black')
for row in range(8, -2, -1):
    for col in range(-1, 9):
        if row == row0 and col == col0:
            print(bishopOne.char(), end='')
        elif bishopOne.canMove(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()