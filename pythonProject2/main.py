import random


class SeaMap:

    def __init__(self):
        self.battleMap = [["[ ]"] * 10 for i in range(10)]
        self.battleMapBot = [["[ ]"] * 10 for i in range(10)]
        self.botMemory = ""
        self.botMemoryCoordinatesNull = 0
        self.botMemoryCoordinatesOne = 0
        # self.creatingShipsAutomatically(self.battleMapBot)
        # print("Как вы хотите создать карту?")
        # self.methodSelection()

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

    def methodSelection(self):
        print("Если в ручную нажмите '1' ")
        print("Если автоматически нажмите '2' ")
        try:
            choiceUser = int(input())
        except Exception:
            print("Вы ввели неверное значение! ")
            print("Попробуйте еще раз")
            self.methodSelection()
        if choiceUser == 1:
            self.creatingShipsMechanically()
        elif choiceUser == 2:
            self.creatingShipsAutomatically(self.battleMap)
            for i in range(10):
                print(self.battleMap[i])
        else:
            print("Вы ввели неверное значение! ")
            print("Попробуйте еще раз")
            self.methodSelection()

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
        print("Расположите еще один четырех-палубный корабль")
        creatingShip(self, 3)
        print("Теперь разместите трех-палубный корабль")
        creatingShip(self, 2)
        print("Расположите еще один трех-палубный корабль")
        creatingShip(self, 2)
        print("Теперь разместите двух-палубный корабль")
        creatingShip(self, 1)
        print("Расположите еще один двух-палубный корабль")
        creatingShip(self, 1)
        print("Теперь разместите один одно-палубный корабль")
        creatingShip(self, 0)
        for i in range(10):
            print(self.battleMap[i])

    def creatingShipsAutomatically(self, map):
        def creatingShip(decks):
            # начало координат корабля
            # map[4][7]="[O]"
            choice = random.randint(1, 2)
            bulinСheck = True
            startNull = random.randint(1, 10)
            startOne = random.randint(1, 10)
            if choice == 1:
                # конец координат корабля
                if startNull + decks < 11 and (decks == 3 or decks == 2 or decks == 1 or decks == 0):
                    for q in range(decks + 3):
                        try:
                            if map[startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][
                                startOne - 1] == "[O]" \
                                    or map[
                                startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][
                                startOne - 2 if startOne - 2 != -1 else startOne - 1] == "[O]" \
                                    or map[
                                startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][startOne] == "[O]":
                                bulinСheck = False
                                creatingShip(decks)
                                break
                        except Exception:
                            pass
                    if bulinСheck:
                        for q in range(decks + 1):
                            map[startNull - 1 + q][startOne - 1] = "[O]"

                elif startNull + decks > 0 and (decks == -3 or decks == -2 or decks == -1):
                    for q in range((-decks) + 3):
                        try:
                            if map[startNull - q if startNull - q != -1 else startNull - q + 1][
                                startOne - 1] == "[O]" \
                                    or map[startNull - q if startNull - q != -1 else startNull - q + 1][
                                startOne - 2 if startOne - 2 != -1 else startOne - 1] == "[O]" \
                                    or map[startNull - q if startNull - q != -1 else startNull - q + 1][
                                startOne] == "[O]":
                                bulinСheck = False
                                creatingShip(decks)
                                break
                        except Exception:
                            pass
                    if bulinСheck:
                        for q in range((-decks) + 1):
                            map[(startNull - 1) - q][startOne - 1] = "[O]"
                else:
                    creatingShip(decks)
            else:
                if startOne + decks < 10 and (decks == 3 or decks == 2 or decks == 1 or decks == 0):  # здесь баг

                    for q in range(decks + 3):
                        try:
                            if map[startNull - 1][
                                startOne - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q] == "[O]" \
                                    or map[startNull - 2 if startNull - 2 != -1 else startNull - 1][
                                startOne - 2 + q if startOne - 2 + q != -1 else startOne - 1 + q] == "[O]" \
                                    or map[startNull if startNull != -1 else startNull + 1][
                                startOne - 2 + q if startOne - 2 + q != -1 else startOne - 1 + q] == "[O]":
                                bulinСheck = False
                                creatingShip(decks)
                                break
                        except Exception:
                            pass
                    if bulinСheck:
                        for q in range(decks + 1):
                            map[startNull - 1][startOne - 1 + q] = "[O]"

                elif startOne + decks > 0 and (decks == -3 or decks == -2 or decks == -1 or decks == 0):

                    for q in range((-decks) + 3):
                        try:
                            if map[startNull - 1][
                                startOne - q if startNull - q != -1 else startNull - 1 - q] == "[O]" \
                                    or map[startNull - 2 if startNull - 2 != -1 else startNull - 1][
                                startOne - q if startOne - q != -1 else startOne - 1 - q] == "[O]" \
                                    or map[startNull if startNull != -1 else startNull - 1][
                                startOne - q if startOne - q != -1 else startOne - 1 - q] == "[O]":
                                bulinСheck = False
                                creatingShip(decks)
                                break
                        except Exception:
                            pass
                    if bulinСheck:
                        for q in range((-decks) + 1):
                            map[startNull - 1][startOne - 1 - q] = "[O]"
                else:
                    creatingShip(decks)

        creatingShip(random.choice([-3, 3]))
        creatingShip(random.choice([-3, 3]))
        creatingShip(random.choice([-2, 2]))
        creatingShip(random.choice([-2, 2]))
        creatingShip(random.choice([-1, 1]))
        creatingShip(random.choice([-1, 1]))
        creatingShip(0)

    def artificialIntelligence(self):
        hitNullNull = 0
        hitOneOne = 0

        def dotsAroundShips(tapy, tapyNullX, tapyOneX):
            if tapy == "x+":
                if self.battleMapBot[tapyNullX][tapyOneX] != "[O]" or self.battleMapBot[hitNull][
                    hitOne] != "[x]":
                    if tapyOneX - 1 == -1:
                        pass
                    else:
                        self.battleMapBot[tapyNullX][tapyOneX - 1] = "[*]"
                        self.battleMapBot[tapyNullX - 1][tapyOneX - 1] = "[*]"
                        self.battleMapBot[tapyNullX + 1][tapyOneX - 1] = "[*]"
                    if self.battleMapBot[tapyNullX][tapyOneX] == "[x]":
                        self.battleMapBot[tapyNullX - 1][tapyOneX] = "[*]"
                        self.battleMapBot[tapyNullX + 1][tapyOneX] = "[*]"
                        if self.battleMapBot[tapyNullX][tapyOneX + 1] == "[x]":
                            self.battleMapBot[tapyNullX - 1][tapyOneX + 1] = "[*]"
                            self.battleMapBot[tapyNullX + 1][tapyOneX + 1] = "[*]"
                            if self.battleMapBot[tapyNullX][tapyOneX + 2] == "[x]":
                                self.battleMapBot[tapyNullX - 1][tapyOneX + 2] = "[*]"
                                self.battleMapBot[tapyNullX + 1][tapyOneX + 2] = "[*]"
                                if self.battleMapBot[tapyNullX][tapyOneX + 3] == "[x]":
                                    self.battleMapBot[tapyNullX - 1][tapyOneX + 3] = "[*]"
                                    self.battleMapBot[tapyNullX + 1][tapyOneX + 3] = "[*]"
                                    if tapyOneX + 4 == 10:
                                        pass
                                    else:
                                        self.battleMapBot[tapyNullX - 1][tapyOneX + 4] = "[*]"
                                        self.battleMapBot[tapyNullX + 1][tapyOneX + 4] = "[*]"
                                        self.battleMapBot[tapyNullX][tapyOneX + 4] = "[*]"
                                else:
                                    self.battleMapBot[tapyNullX - 1][tapyOneX + 3] = "[*]"
                                    self.battleMapBot[tapyNullX + 1][tapyOneX + 3] = "[*]"
                                    self.battleMapBot[tapyNullX][tapyOneX + 3] = "[*]"
                            else:
                                self.battleMapBot[tapyNullX - 1][tapyOneX + 2] = "[*]"
                                self.battleMapBot[tapyNullX + 1][tapyOneX + 2] = "[*]"
                                self.battleMapBot[tapyNullX][tapyOneX + 2] = "[*]"
                        else:
                            self.battleMapBot[tapyNullX - 1][tapyOneX + 1] = "[*]"
                            self.battleMapBot[tapyNullX + 1][tapyOneX + 1] = "[*]"
                            self.battleMapBot[tapyNullX][tapyOneX + 1] = "[*]"

        def cheekShoot(hitNull, hitOne, tapy):
            # проверяет уничтожен корабль или нет
            if tapy == "hitOne+":
                if self.battleMapBot[hitNull][hitOne + 1] == "[x]":
                    if self.battleMapBot[hitNull][hitOne + 2] == "[x]":
                        if self.battleMapBot[hitNull][hitOne + 3] == "[x]":
                            if hitOne + 4 == 10:
                                print("Бот уничтожил твой корабль! ")
                                # передаем в метод для раставления точек
                                dotsAroundShips("x+", hitNull, hitOne)
                                return True
                            elif self.battleMapBot[hitNull][hitOne + 4] == "[*]" or self.battleMapBot[hitNull][
                                hitOne + 4] == "[ ]":
                                print("Бот уничтожил твой корабль! ")
                                # передаем в метод для раставления точек
                                dotsAroundShips("x+", hitNull, hitOne)
                                return True
                            else:
                                return False
                        else:
                            if self.battleMapBot[hitNull][hitOne + 3] == "[x]" or self.battleMapBot[hitNull][
                                hitOne + 3] == "[ ]" or self.battleMapBot[hitNull][hitOne + 3] == "[*]" or (
                                    hitOne + 3) == 10:
                                print("Бот уничтожил твой корабль! ")
                                # передаем в метод для раставления точек
                                dotsAroundShips("x+", hitNull, hitOne)
                                return True
                            else:
                                return False
                    else:
                        if self.battleMapBot[hitNull][hitOne + 2] == "[x]" or self.battleMapBot[hitNull][
                            hitOne + 2] == "[ ]" or self.battleMapBot[hitNull][hitOne + 2] == "[*]" or (
                                hitOne + 2) == 10:
                            print("Бот уничтожил твой корабль! ")
                            # передаем в метод для раставления точек
                            dotsAroundShips("x+", hitNull, hitOne)
                            return True
                        else:
                            return False
                else:
                    if self.battleMapBot[hitNull][hitOne + 1] == "[x]" or self.battleMapBot[hitNull][
                        hitOne + 1] == "[*]" or self.battleMapBot[hitNull][
                        hitOne + 1] == "[ ]" or (hitOne + 1) == 10:
                        print("Бот уничтожил твой корабль! ")
                        # передаем в метод для раставления точек
                        dotsAroundShips("x+", hitNull, hitOne)
                        return True
                    else:
                        return False

        def directionAlgorithm(hitNull, hitOne, direction):
            if direction == "horizontal+":
                if hitOne + 1 == 10:
                    if self.battleMapBot[hitNullNull][hitOneOne - 1] == "[ ]" or self.battleMapBot[hitNullNull][
                        hitOneOne - 1] == "[*]" :
                        # проверяет уничтожен корабль или нет
                        print("Бот уничтожил твой корабль! ")
                        # передаем в метод для раставления точек
                        dotsAroundShips("x+", hitNullNull, hitOneOne)
                        return True
                    else:
                        return False
                if self.battleMapBot[hitNull][hitOne + 1] != "[*]" or self.battleMapBot[hitNull][
                    hitOne + 1] != "[x]" :
                    if self.battleMapBot[hitNull][hitOne + 1] == "[O]":
                        self.battleMapBot[hitNull][hitOne + 1] = "[x]"
                        directionAlgorithm(hitNull, hitOne + 1, "horizontal+")
                        # проходит и уничтожает до конца
                    else:
                        if self.battleMapBot[hitNullNull][hitOneOne - 1] == "[ ]" or self.battleMapBot[hitNullNull][
                            hitOneOne - 1] == "[*]" or (hitOneOne - 1) == -1:
                            #баг ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                            # проверяет уничтожен корабль или нет
                            print("Бот уничтожил твой корабль! ")
                            # передаем в метод для раставления точек
                            dotsAroundShips("x+", hitNullNull, hitOneOne)
                            return True
                        else:
                            self.battleMapBot[hitNull][hitOne + 1] = "[*]"
                            return False
            elif direction == "horizontal-":
                if self.battleMapBot[hitNull][hitOne - 1] != "[*]" or self.battleMapBot[hitNull][
                    hitOne - 1] != "[x]" or (hitOne - 1) != -1:
                    if self.battleMapBot[hitNull][hitOne - 1] == "[O]":
                        self.battleMapBot[hitNull][hitOne - 1] = "[x]"
                        directionAlgorithm(hitNull, hitOne - 1, "horizontal-")
                        # проходит и уничтожает до конца
                    else:
                        if cheekShoot(hitNull, hitOne, "hitOne+"):
                            return True
                        else:
                            self.battleMapBot[hitNull][hitOne - 1] = "[*]"
                            return False

        def demolitionAlgorithm(hitNull, hitOne):
            # проверяем однопалубный корабль ЗДЕЛАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! (hitNull - 1) == -1 or (hitNull + 1) == 10
            if hitOne + 1 == 10:
                if (self.battleMapBot[hitNull][hitOne - 1] != "[O]" and self.battleMapBot[hitNull][
                    hitOne - 1] != "[x]") \
                        and (self.battleMapBot[hitNull - 1][hitOne] != "[O]" and self.battleMapBot[hitNull - 1][
                    hitOne] != "[x]") \
                        and (self.battleMapBot[hitNull + 1][hitOne] != "[O]" and self.battleMapBot[hitNull + 1][
                    hitOne] != "[x]"):
                    if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
                        self.botMemory = ""
                        return True
            if hitOne - 1 == -1:
                if (self.battleMapBot[hitNull][hitOne + 1] != "[O]" and self.battleMapBot[hitNull][
                    hitOne + 1] != "[x]") \
                        and (self.battleMapBot[hitNull - 1][hitOne] != "[O]" and self.battleMapBot[hitNull - 1][
                    hitOne] != "[x]") \
                        and (self.battleMapBot[hitNull + 1][hitOne] != "[O]" and self.battleMapBot[hitNull + 1][
                    hitOne] != "[x]"):
                    if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
                        self.botMemory = ""
                        return True

            # проверяем направление в x- прижата к границе
            if(hitOne + 1) == 10:
                if (self.battleMapBot[hitNull][hitOne - 1] != "[*]" or self.battleMapBot[hitNull][
                    hitOne - 1] != "[x]") \
                        and (self.botMemory == "x-" or self.botMemory == ""):
                    if self.battleMapBot[hitNull][hitOne - 1] == "[O]":
                        self.battleMapBot[hitNull][hitOne - 1] = "[x]"
                        # направление подтвердилось проверяем дальше
                        if directionAlgorithm(hitNull, hitOne - 1, "horizontal-") == True:
                            self.botMemory = ""
                            return True
                        else:
                            self.botMemory = "x+"
                            self.botMemoryCoordinatesNull = hitNull
                            self.botMemoryCoordinatesOne = hitOne
                            return False

                    else:
                        self.battleMapBot[hitNull][hitOne - 1] = "[*]"
                        self.botMemory = "x+"
                        self.botMemoryCoordinatesNull = hitNull
                        self.botMemoryCoordinatesOne = hitOne
                        return False
            # проверяем направление в x+ прижата к границе
            if hitOne - 1 == -1:
                if (self.battleMapBot[hitNull][hitOne + 1] != "[*]" or self.battleMapBot[hitNull][hitOne + 1] != "[x]") \
                        and (self.botMemory == "x+" or self.botMemory == ""):
                    if self.battleMapBot[hitNull][hitOne + 1] == "[O]":
                        self.battleMapBot[hitNull][hitOne + 1] = "[x]"
                        # направление подтвердилось проверяем дальше
                        if directionAlgorithm(hitNull, hitOne + 1, "horizontal+") == True:
                            self.botMemory = ""
                            return True
                        else:
                            self.botMemory = "x-"
                            self.botMemoryCoordinatesNull = hitNullNull
                            self.botMemoryCoordinatesOne = hitOneOne
                            return False

                    else:
                        self.battleMapBot[hitNull][hitOne + 1] = "[*]"
                        self.botMemory = "x-"
                        self.botMemoryCoordinatesNull = hitNull
                        self.botMemoryCoordinatesOne = hitOne
                        return False
            # проверяем направление в x+
            if (self.battleMapBot[hitNull][hitOne + 1] != "[*]" or self.battleMapBot[hitNull][hitOne + 1] != "[x]") \
                    and (self.botMemory == "x+" or self.botMemory == ""):
                if self.battleMapBot[hitNull][hitOne + 1] == "[O]":
                    self.battleMapBot[hitNull][hitOne + 1] = "[x]"
                    # направление подтвердилось проверяем дальше
                    if directionAlgorithm(hitNull, hitOne + 1, "horizontal+") == True:
                        self.botMemory = ""
                        return True
                    else:
                        self.botMemory = "x-"
                        self.botMemoryCoordinatesNull = hitNullNull
                        self.botMemoryCoordinatesOne = hitOneOne
                        return False

                else:
                    self.battleMapBot[hitNull][hitOne + 1] = "[*]"
                    self.botMemory = "x-"
                    self.botMemoryCoordinatesNull = hitNull
                    self.botMemoryCoordinatesOne = hitOne
                    return False
            # проверяем направление в x-
            if (self.battleMapBot[hitNull][hitOne - 1] != "[*]" or self.battleMapBot[hitNull][
                hitOne - 1] != "[x]" ) \
                    and (self.botMemory == "x-" or self.botMemory == ""):
                if self.battleMapBot[hitNull][hitOne - 1] == "[O]":
                    self.battleMapBot[hitNull][hitOne - 1] = "[x]"
                    # направление подтвердилось проверяем дальше
                    if directionAlgorithm(hitNull, hitOne - 1, "horizontal-") == True:
                        self.botMemory = ""
                        return True
                    else:
                        self.botMemory = "x+"
                        self.botMemoryCoordinatesNull = hitNull
                        self.botMemoryCoordinatesOne = hitOne
                        return False

                else:
                    self.battleMapBot[hitNull][hitOne - 1] = "[*]"
                    self.botMemory = "x+"
                    self.botMemoryCoordinatesNull = hitNull
                    self.botMemoryCoordinatesOne = hitOne
                    return False


        if self.botMemory != "":
            if self.botMemory == "x+":
                hitNull = self.botMemoryCoordinatesNull
                hitOne = self.botMemoryCoordinatesOne
            if self.botMemory == "x-":
                hitNull = self.botMemoryCoordinatesNull
                hitOne = self.botMemoryCoordinatesOne-1
        else:
            #баг----------------------------------------------------------------------------------------------------------------------------------------------------
            hitNull =9# random.randint(0, 9)
            hitOne =0# random.randint(0, 9)
            a.battleMapBot[9][0] = "[O]"
            a.battleMapBot[9][1] = "[O]"
            a.battleMapBot[9][2] = "[O]"
            a.battleMapBot[9][3] = "[O]"

        if self.battleMapBot[hitNull][hitOne] == "[ ]":
            self.battleMapBot[hitNull][hitOne] = "[*]"
            return False
            # промазал
        else:
            if self.battleMapBot[hitNull][hitOne] == "[*]" or self.battleMapBot[hitNull][hitOne] == "[x]":
                self.artificialIntelligence()
                # не трогать
            else:
                # попал
                self.battleMapBot[hitNull][hitOne] = "[x]"
                # обозначить
                hitNullNull = hitNull
                hitOneOne = hitOne
                print(hitNull, hitOne)
                # передать для определения направления
                demolitionAlgorithm(hitNull, hitOne)
                return True



a = SeaMap()
a.artificialIntelligence()
for i in range(10):
             print(a.battleMapBot[i])
a.artificialIntelligence()
for i in range(10):
             print(a.battleMapBot[i])
# a.artificialIntelligence()
# a.battleMapBot[2][1]= "[O]"
# a.battleMapBot[2][2]="[O]"
# a.battleMapBot[2][3]= "[O]"
# a.battleMapBot[2][4]= "[O]"
#
# a.battleMapBot[4][1]= "[O]"
# a.battleMapBot[4][2]="[O]"
# a.battleMapBot[4][3]= "[O]"
# a.battleMapBot[4][4]= "[O]"
#
# a.battleMapBot[6][1]= "[O]"
# a.battleMapBot[6][2]="[O]"
# a.battleMapBot[6][3]= "[O]"
# a.battleMapBot[6][4]= "[O]"
#
# a.battleMapBot[8][1]= "[O]"
# a.battleMapBot[8][2]="[O]"
# a.battleMapBot[8][3]= "[O]"
# a.battleMapBot[8][4]= "[O]"
#
#
# for i in range(10):
#     print(a.battleMapBot[i])
# while True:
#     print("qqq")
#     q = input()
#     if q == "v":
#         a.artificialIntelligence()
#         for i in range(10):
#             print(a.battleMapBot[i])
#     else:
#         break
