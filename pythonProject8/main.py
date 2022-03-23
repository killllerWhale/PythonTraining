class Pawn(Piece):
   ch = 'P'

   def check_move(self, row: int, col: int, row1: int, col1: int):
       """Проверка перемещения фигуру из точки (row, col) в точку (row1, col1).
       Если перемещение возможно, метод выполнит его и вернет True.
       Если нет --- вернет False"""
       check = self.check()  # Есть ли шах к перед ходом
       if not correct_coords(row, col) or not correct_coords(row1, col1):
           return False
       if row == row1 and col == col1:
           return False  # нельзя пойти в ту же клетку
       piece = self.field[row][col]
       target = self.field[row1][col1]
       if piece is None:
           return False
       if piece.get_color() != self.color:
           return False

       if isinstance(piece, King) and self.is_under_attack(row1, col1, opponent(self.current_player_color())):
           return False

       if not (piece.can_move(self.field, row, col, row1, col1) and target is None) and \
               not (piece.can_attack(self.field, row, col, row1, col1) and
                    (target is not None and not isinstance(target, King)
                     and target.get_color() == opponent(self.current_player_color()))):
           return False

       old_field = [x.copy() for x in self.field]  # Сохранить поле
       self.field[row][col] = None  # Снять фигуру.
       self.field[row1][col1] = piece  # Поставить на новое место.
       if check and self.check():  # В результате хода избежать шаха не удалось
           # Возвращаемся в исходное состояние
           self.field = old_field
           return False
       # Возвращаемся в исходное состояние
       self.field = old_field
       return True

   def move_piece(self, row, col, row1, col1):
       """Переместить фигуру из точки (row, col) в точку (row1, col1).
       Если перемещение возможно, метод выполнит его и вернет True.
       Если нет --- вернет False"""
       if self.check_move(row, col, row1, col1):
           piece = self.field[row][col]
           self.field[row][col] = None  # Снять фигуру.
           piece.moved()
           self.field[row1][col1] = piece  # Поставить на новое место.
           if self.check_promotion(piece, row1):
               self.promotion = True
           self.color = opponent(self.color)
           self.change = True
           return True
       return False

   def is_under_attack(self, row, col, color):
       for row1 in range(8):
           for col1 in range(8):
               if self.field[row1][col1] is not None:
                   if self.field[row1][col1].get_color() == color and \
                           self.field[row1][col1].can_attack(self.field, row1, col1, row, col):
                       return True
       return False


   def can_move(self, board, row, col, row1, col1):
       # Пешка может ходить только по вертикали
       # "взятие на проходе" не реализовано
       if col != col1:
           return False

       if not self.is_path_clear(board, row, col, row1, col1):
           return False

       # Пешка может сделать из начального положения ход на 2 клетки
       # вперёд, поэтому поместим индекс начального ряда в start_row.
       if self.color == WHITE:
           direction = 1
           start_row = 1
       else:
           direction = -1
           start_row = 6

       # ход на 1 клетку
       if row + direction == row1:
           return True

       # ход на 2 клетки из начального положения
       if row == start_row and row + 2 * direction == row1:
           return True

       return False

   def can_attack(self, board, row, col, row1, col1):
       direction = 1 if (self.color == WHITE) else -1
       return (row + direction == row1
               and (col + 1 == col1 or col - 1 == col1))

class Rook(Piece):
   ch = 'R'

   def can_move(self, board, row, col, row1, col1):
       # Невозможно сделать ход в клетку, которая не лежит в том же ряду
       # или столбце клеток.
       if row != row1 and col != col1:
           return False
       if not self.is_path_clear(board, row, col, row1, col1):
           return False

       return True

class Knight(Piece):
   ch = 'N'

   def can_move(self, board, row, col, row1, col1):
       # Конь двигается буквой Г (2 вертикально, 1 горизонтально)
       if abs(row - row1) == 2 and abs(col - col1) == 1:
           return True
       # Конь двигается буквой Г (1 вертикально, 2 горизонтально)
       if abs(row - row1) == 1 and abs(col - col1) == 2:
           return True

       return False

class Bishop(Piece):
   ch = 'B'

   def can_move(self, board, row, col, row1, col1):

       if not self.is_path_clear(board, row, col, row1, col1):
           return False

       # Слон двигается по диагонали
       # Смещение по строка должно равняться смещению по столбцам
       if abs(row - row1) == abs(col - col1):
           return True

       return False

class Queen(Piece):
   ch = 'Q'

   def can_move(self, board, row, col, row1, col1):

       if not self.is_path_clear(board, row, col, row1, col1):
           return False

       # Ферзь двигается вертикально
       if col == col1:
           return True

       # Ферзь двигается горизонтально
       if row == row1:
           return True

       # Ферзь двигается по диагонали
       # Смещение по строка должно равняться смещению по столбцам
       if abs(row - row1) == abs(col - col1):
           return True

       return False


class King(Piece):
   ch = 'K'

   def can_move(self, board, row, col, row1, col1):

       if not self.is_path_clear(board, row, col, row1, col1):
           return False

       # Король двигается в любую клетку с рассотоянием равным 1
       if max(abs(row - row1), abs(col - col1)) == 1:
           return True

       return False

