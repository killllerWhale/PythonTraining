import random


class SeaMap:

    def __init__(self):
        self.battleMap = [["[ ]"] * 10 for i in range(10)]
        self.battleMapBot = [["[ ]"] * 10 for i in range(10)]
        # self.creatingShipsMechanically()
        self.creatingShipsAutomatically()

    def shoot(self, row, col):
        check = self.battleMapBot[row][col]
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

    def creatingShipsMechanically(self):
        def shipsNearbyHorizontal(player, row, col, decks):
            if player.battleMap[row][col] != "[O]" and player.battleMap[row][col - decks] != "[O]":
                for i in range(decks + 1):
                    if player.battleMap[row - 1][(col) - i] == "[O]":
                        return False
                    if player.battleMap[row + 1][(col) - i] == "[O]":
                        return False
                return True

        def shipsNearbyVertical(player, col, row, decks):
            if player.battleMap[row][col] != "[O]" and player.battleMap[row - decks][col] != "[O]":
                for i in range(decks + 1):
                    if player.battleMap[row - i][col - 1] == "[O]":
                        return False
                    if player.battleMap[row - i][col + 1] == "[O]":
                        return False
                return True

        def creatingShip(player, decks):
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
                            if shipsNearbyHorizontal(player, startNull - 1, (startOne) + decks, decks + 2):
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
                            if shipsNearbyHorizontal(player, endNull - 1, (endOne) + decks, decks + 2):
                                for q in range(endOne, (endOne) + decks + 1):
                                    player.battleMap[startNull - 1][q - 1] = "[O]"
                            else:
                                print("Корабль слишком близок к другому ! ")
                                creatingShip(player, decks)

                    else:
                        if result == -decks:
                            for q in range(startNull, startNull + decks + 1):
                                if player.battleMap[q - 1][startOne - 1] == "[O]":
                                    print("Эти координаты заняты! ")
                                    creatingShip(player, decks)
                                    break
                            if shipsNearbyVertical(player, startOne - 1, (startNull) + decks, decks + 1):
                                for q in range(startNull, startNull + decks + 1):
                                    player.battleMap[q - 1][startOne - 1] = "[O]"
                            else:
                                print("Корабль слишком близок к другому ! ")
                                creatingShip(player, decks)

                        else:
                            for q in range(endNull, endNull + decks + 1):
                                if player.battleMap[q - 1][startOne - 1] == "[O]":
                                    print("Эти координаты заняты! ")
                                    creatingShip(player, decks)
                                    break
                            if shipsNearbyVertical(player, endOne - 1, (endNull) + decks, decks + 1):
                                for q in range(endNull, endNull + decks + 1):
                                    player.battleMap[q - 1][endOne - 1] = "[O]"
                            else:
                                print("Корабль слишком близок к другому ! ")
                                creatingShip(player, decks)

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

    def creatingShipsAutomatically(self):
        def creatingShip(player, decks):
            # начало координат корабля
            #self.battleMapBot[9][0] = "[O]"
            choice = 1 #random.randint(1,2)
            bulinСheck = True
            startNull =  random.randint(1,10)
            startOne =  random.randint(1,10)
            print(str(startNull)+" "+str(startOne)+" "+str(choice)+" "+str(decks))
            if choice == 1:
                # конец координат корабля
                if startNull + decks < 11 and (decks == 3 or decks == 2 or decks == 1 or decks == 0) :
                    for q in range(decks + 3):
                        try:
                            if player.battleMapBot[startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][startOne - 1] == "[O]" \
                                    or player.battleMapBot[startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][startOne - 2 if startOne - 2 != -1 else startOne - 1] == "[O]" \
                                    or player.battleMapBot[startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][startOne] == "[O]":
                                bulinСheck = False
                                creatingShip(player, decks)
                                break
                        except Exception:
                            pass
                    if bulinСheck:
                        for q in range(decks + 1):
                            player.battleMapBot[startNull - 1 + q][startOne - 1] = "[O]"



                elif startNull + decks > 0 and (decks == -3 or decks == -2 or decks == -1 ):
                    for q in range((-decks) + 3):
                        try:
                            if player.battleMapBot[startNull - q if startNull - q != -1 else startNull - q+1][startOne - 1] == "[O]" \
                                    or player.battleMapBot[startNull - q if startNull - q != -1 else startNull - q+1][startOne - 2 if startOne - 2 != -1 else startOne - 1] == "[O]" \
                                    or player.battleMapBot[startNull - q if startNull - q != -1 else startNull - q+1][startOne] == "[O]":
                                bulinСheck = False
                                creatingShip(player, decks)
                                break
                        except Exception:
                            pass
                    if bulinСheck:
                        for q in range((-decks) + 1):
                            player.battleMapBot[(startNull-1) - q][startOne - 1] = "[O]"
                else:
                    creatingShip(player, decks)
            # else:
            #     if startOne + decks < 10 and decks == 3:
            #         for q in range(decks + 1):
            #             if player.battleMapBot[startNull - 1][(startOne - 1) + q] == "[O]":
            #                 creatingShip(player, decks)
            #                 break
            #         if shipsNearbyHorizontalPlus(player, startNull-1, startOne-1, decks):
            #             for q in range(decks + 1):
            #                 player.battleMapBot[startNull - 1][startOne - 1 + q] = "[O]"
            #         else:
            #             creatingShip(player, decks)
            #     elif startOne + decks > 0 and decks == -3:
            #         for q in range((-decks) + 1):
            #             if player.battleMapBot[startNull - 1][(startOne - 1) - q] == "[O]":
            #                 creatingShip(player, decks)
            #                 break
            #         if shipsNearbyHorizontalMinus(player, startNull - 1, startOne - 1, decks):
            #             for q in range((-decks) + 1):
            #                 player.battleMapBot[startNull - 1][startOne - 1 - q] = "[O]"
            #         else:
            #             creatingShip(player, decks)
            #     else:
            #         creatingShip(player, decks)

        creatingShip(self, random.choice([-3,3]))
        creatingShip(self, random.choice([-3, 3]))
        creatingShip(self, random.choice([-2, 2]))
        creatingShip(self, random.choice([-2, 2]))
        creatingShip(self, random.choice([-1, 1]))
        creatingShip(self, 0)




        # random.choice([-3,3])
        for i in range(10):
            print(self.battleMapBot[i])

    # def artificialIntelligence(self):
    #     pass


a = SeaMap()


