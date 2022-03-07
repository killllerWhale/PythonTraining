class SeaMap:

    def __init__(self):
        self.battleMap = [["[ ]"] * 10 for i in range(10)]
        self.creatingShips()

    def shoot(self, row, col):
        check = self.battleMap[row][col]
        if check == "x":
            print("Вы сюда стреляли! Попробуйте еще раз...")
            print("Введите кординаты: ")
            self.shoot(int(input()), int(input()))
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
        def shipsNearby(player , row, col, decks):
            if player.battleMap[row][col] != "[O]" and player.battleMap[row][col - decks] != "[O]":
                for i in range(decks-1):
                    if player.battleMap[row-1][(col-1)-i] == "[O]":
                        return False
                    if player.battleMap[row+1][(col-1)-i] == "[O]":
                        return False
                return True





        def creatingShip(player, decks):
            self.battleMap[4][3] = "[O]"
            self.battleMap[0][6] = "[O]"
            for i in range(10):
                print(self.battleMap[i])
            print("введите начало координат корабля: ")
            start = input().split()
            startNull = int(start[0])
            startOne = int(start[1])
            if (-1 < startNull < 11) and (-1 < startOne < 11):
                print("введите конец координат корабля: ")
                end = input().split()
                endNull = int(end[0])
                endOne = int(end[1])
                result = startNull - endNull + startOne - endOne
                if (-1 < endNull < 11) and (-1 < endOne < 11) and (result == decks or result == (-decks)):
                    if startNull == endNull:
                        if result == -decks:
                            for q in range(startOne, (startOne) + decks + 1):
                                if player.battleMap[startNull - 1][q - 1] == "[O]":
                                    print("Эти координаты заняты! ")
                                    creatingShip(player, decks)
                                    break
                            if shipsNearby(player , startNull-1, (startOne) + decks, decks+2):
                                for q in range(startOne, (startOne) + decks + 1):
                                    player.battleMap[startNull - 1][q - 1] = "[O]"
                            else:
                                print("Корабль слишком близок к другому ! ")
                                creatingShip(player, decks)



                        else:
                            for q in range(endOne, (endOne) + decks + 1):
                                if player.battleMap[startNull - 1][q - 1] == "[O]":
                                    print("Эти координаты заняты! ")
                                    creatingShip(player, decks)
                                    break
                            for q in range(endOne, (endOne) + decks + 1):
                                player.battleMap[startNull - 1][q - 1] = "[O]"

                    else:
                        if result == -decks:
                            for q in range(startNull, startNull + decks + 1):
                                if player.battleMap[q - 1][startOne - 1] == "[O]":
                                    print("Эти координаты заняты! ")
                                    creatingShip(player, decks)
                                    break
                            for q in range(startNull, startNull + decks + 1):
                                player.battleMap[q - 1][startOne - 1] = "[O]"

                        else:
                            for q in range(endNull, endNull + decks + 1):
                                if player.battleMap[q - 1][startOne - 1] == "[O]":
                                    print("Эти координаты заняты! ")
                                    creatingShip(player, decks)
                                    break
                            for q in range(endNull, endNull + decks + 1):
                                player.battleMap[q - 1][startOne - 1] = "[O]"

                else:
                    print("Вы неправильно ввели координаты ")
                    creatingShip(player, decks)


            else:
                print("Вы неправильно ввели координаты ")
                creatingShip(player, decks)


        print("Нужно расставить пять короблей по полю:"
              " 1 - четырех палубный , 1 - трех палубный, 2 - двух палубных ")


        print("Начнем с четырех-палубнуго корабля")
        creatingShip(self, 3)
        print("Теперь разместите трех-палубный корабль")
        creatingShip(self, 2)
        print("Теперь разместите двух-палубный корабль")
        creatingShip(self, 1)
        print("Теперь разместите двух-палубный корабль")
        creatingShip(self, 1)
        for i in range(10):
            print(self.battleMap[i])


a = SeaMap()
