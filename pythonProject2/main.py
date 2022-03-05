class SeaMap:

    def __init__(self):
        self.battleMap = [["[ ]"] * 10 for i in range(10)]
        self.creatingShips()

    def shoot(self, row, col):
        check = self.battleMap[row][col]
        if check == "x":
            print("Вы сюда стреляли! Попробуйте еще раз...")
            print("Введите кординаты: ")
            self.shoot(int(input()),int(input()))
        if check == "[]":
            print("Вы промазали! ")
            return False
        if check == "О":
            print("Вы попали!")
            print("Введите кординаты: ")
            self.shoot(int(input()), int(input()))
        else:
            print("Вы ввели что то не так")
            print("Введите кординаты: ")
            self.shoot(int(input()), int(input()))

    def creatingShips(self):
        def creatingShip(player, decks):
            print("введите начало координат корабля: ")
            start = input().split()
            if (-1<int(start[0])<10) and (-1<int(start[1])<10) and player.battleMap[int(start[0])][int(start[1])]!="О":
                print("введите конец координат корабля: ")
                end = input().split()
                result = int(start[0])-int(end[0])+int(start[1])-int(end[1])
                if (-1< int(end[0])<10) and (-1< int(end[1])<10) and (result==decks or result==(-decks)):
                    if int(start[0])==int(end[0]):
                        if result == -decks:
                            for q in range(decks+1):
                                if player.battleMap[int(start[0])][q] != "[O]":
                                    player.battleMap[int(start[0])][q] = "[O]"
                                else:
                                    print("Error! ")

                        else:
                            for q in range(decks + 1):
                                if player.battleMap[int(start[0])][q] != "[O]":
                                    player.battleMap[int(start[0])][q] = "[O]"
                                else:
                                    print("Error! ")

                    else:
                        if result == -decks:
                            for q in range(decks + 1):
                                if player.battleMap[q][int(start[1])] != "[O]":
                                    player.battleMap[q][int(start[1])] = "[O]"
                                else:
                                    print("Error! ")

                        else:
                            for q in range(decks + 1):
                                if player.battleMap[q][int(start[1])] != "[O]":
                                    player.battleMap[q][int(start[1])] = "[O]"
                                else:
                                    print("Error! ")

                else:
                    print("Error! ")

            else:
                print("Error! ")



        print("Нужно расставить пять короблей по полю:"
              " 1 - четырех палубный , 2 - трех палубных, 2 - двух палубных ")

        print("Начнем с четырех палубнуго")
        creatingShip(self, 3)
        for i in range(10):
            print(self.battleMap[i])


a = SeaMap()
