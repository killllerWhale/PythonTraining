import random
import time


class SeaMap:

    def __init__(self):
        self.battleMap = [["[ ]"] * 10 for i in range(10)]
        self.battleMapBot = [["[ ]"] * 10 for i in range(10)]
        self.battleMapBot_view = [["[ ]"] * 10 for i in range(10)]
        self.botMemory = ""
        self.botMemoryCoordinatesNull = 0
        self.botMemoryCoordinatesOne = 0

    def shoot(self, row, col):
        check = self.battleMapBot[row][col]
        if check == "[x]" or check == "[*]":
            print("Вы сюда стреляли! Попробуйте еще раз...")
            return True
        if check == "[ ]":
            self.battleMapBot[row][col] = "[*]"
            self.battleMapBot_view[row][col] = "[*]"
            print("Вы промазали! ")
            return False
        if check == "[О]":
            print("Вы попали!")
            self.battleMapBot[row][col] = "[x]"
            self.battleMapBot_view[row][col] = "[x]"
            return True
        else:
            print("Вы ввели что то не так")
            return True

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
            print("\n                       Отлично вот ваша карта! ")
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
            choice = 2  # random.randint(1, 2)
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
                if self.battleMap[tapyNullX][tapyOneX] != "[O]" or self.battleMap[hitNull][
                    hitOne] != "[x]":
                    if tapyOneX - 1 != -1:
                        if tapyNullX - 1 != -1:
                            self.battleMap[tapyNullX - 1][tapyOneX - 1] = "[*]"
                        if tapyNullX + 1 != 10:
                            self.battleMap[tapyNullX + 1][tapyOneX - 1] = "[*]"
                        self.battleMap[tapyNullX][tapyOneX - 1] = "[*]"
                    if self.battleMap[tapyNullX][tapyOneX] == "[x]":
                        if tapyNullX - 1 != -1:
                            self.battleMap[tapyNullX - 1][tapyOneX] = "[*]"
                        if tapyNullX + 1 != 10:
                            self.battleMap[tapyNullX + 1][tapyOneX] = "[*]"
                        if tapyOneX + 1 != 10:
                            if self.battleMap[tapyNullX][tapyOneX + 1] == "[x]":
                                if tapyNullX - 1 != -1:
                                    self.battleMap[tapyNullX - 1][tapyOneX + 1] = "[*]"
                                if tapyNullX + 1 != 10:
                                    self.battleMap[tapyNullX + 1][tapyOneX + 1] = "[*]"
                                if tapyOneX + 2 != 10:
                                    if self.battleMap[tapyNullX][tapyOneX + 2] == "[x]":
                                        if tapyNullX - 1 != -1:
                                            self.battleMap[tapyNullX - 1][tapyOneX + 2] = "[*]"
                                        if tapyNullX + 1 != 10:
                                            self.battleMap[tapyNullX + 1][tapyOneX + 2] = "[*]"
                                        if tapyOneX + 3 != 10:
                                            if self.battleMap[tapyNullX][tapyOneX + 3] == "[x]":
                                                if tapyNullX - 1 != -1:
                                                    self.battleMap[tapyNullX - 1][tapyOneX + 3] = "[*]"
                                                if tapyNullX + 1 != 10:
                                                    self.battleMap[tapyNullX + 1][tapyOneX + 3] = "[*]"
                                                if tapyOneX + 4 != 10:
                                                    if tapyNullX - 1 != -1:
                                                        self.battleMap[tapyNullX - 1][tapyOneX + 4] = "[*]"
                                                    if tapyNullX + 1 != 10:
                                                        self.battleMap[tapyNullX + 1][tapyOneX + 4] = "[*]"
                                                    self.battleMap[tapyNullX][tapyOneX + 4] = "[*]"
                                            else:
                                                if tapyNullX - 1 != -1:
                                                    self.battleMap[tapyNullX - 1][tapyOneX + 3] = "[*]"
                                                if tapyNullX + 1 != 10:
                                                    self.battleMap[tapyNullX + 1][tapyOneX + 3] = "[*]"
                                                self.battleMap[tapyNullX][tapyOneX + 3] = "[*]"
                                    else:

                                        if tapyNullX - 1 != -1:
                                            self.battleMap[tapyNullX - 1][tapyOneX + 2] = "[*]"
                                        if tapyNullX + 1 != 10:
                                            self.battleMap[tapyNullX + 1][tapyOneX + 2] = "[*]"
                                        self.battleMap[tapyNullX][tapyOneX + 2] = "[*]"

                            else:
                                if tapyNullX - 1 != -1:
                                    if tapyOneX + 1 != 10:
                                        self.battleMap[tapyNullX - 1][tapyOneX + 1] = "[*]"
                                if tapyNullX + 1 != 10:
                                    if tapyOneX + 1 != 10:
                                        self.battleMap[tapyNullX + 1][tapyOneX + 1] = "[*]"
                                if tapyOneX + 1 != 10:
                                    self.battleMap[tapyNullX][tapyOneX + 1] = "[*]"

        def cheekShoot(hitNull, hitOne, tapy):
            # проверяет уничтожен корабль или нет

            if tapy == "hitOne+":
                if self.battleMap[hitNull][hitOne + 1] == "[x]":
                    if self.battleMap[hitNull][hitOne + 2] == "[x]":
                        if hitOne+3 != 10:
                            if self.battleMap[hitNull][hitOne + 3] == "[x]":
                                if hitOne + 4 == 10:
                                    print("Бот уничтожил твой корабль! ")
                                    # передаем в метод для раставления точек
                                    dotsAroundShips("x+", hitNull, hitOne)
                                    self.botMemory = ""
                                    return True
                                elif self.battleMap[hitNull][hitOne + 4] == "[*]" or self.battleMap[hitNull][
                                    hitOne + 4] == "[ ]":
                                    print("Бот уничтожил твой корабль! ")
                                    # передаем в метод для раставления точек
                                    dotsAroundShips("x+", hitNull, hitOne)
                                    self.botMemory = ""
                                    return True
                                else:
                                    return False
                            else:
                                if self.battleMap[hitNull][hitOne + 3] == "[x]" or self.battleMap[hitNull][
                                    hitOne + 3] == "[ ]" or self.battleMap[hitNull][hitOne + 3] == "[*]" or (
                                        hitOne + 3) == 10:
                                    print("Бот уничтожил твой корабль! ")
                                    # передаем в метод для раставления точек
                                    dotsAroundShips("x+", hitNull, hitOne)
                                    self.botMemory = ""
                                    return True
                                else:
                                    return False
                        else:
                            print("Бот уничтожил твой корабль! ")
                            # передаем в метод для раставления точек
                            dotsAroundShips("x+", hitNull, hitOne)
                            self.botMemory = ""
                            return True
                    else:
                        if self.battleMap[hitNull][hitOne + 2] == "[x]" or self.battleMap[hitNull][
                            hitOne + 2] == "[ ]" or self.battleMap[hitNull][hitOne + 2] == "[*]" or (
                                hitOne + 2) == 10:
                            print("Бот уничтожил твой корабль! ")
                            # передаем в метод для раставления точек
                            dotsAroundShips("x+", hitNull, hitOne)
                            self.botMemory = ""
                            return True
                        else:
                            return False
                else:
                    if self.battleMap[hitNull][hitOne + 1] == "[x]" or self.battleMap[hitNull][
                        hitOne + 1] == "[*]" or self.battleMap[hitNull][
                        hitOne + 1] == "[ ]" or (hitOne + 1) == 10:
                        print("Бот уничтожил твой корабль! ")
                        # передаем в метод для раставления точек
                        dotsAroundShips("x+", hitNull, hitOne)
                        self.botMemory = ""
                        return True
                    else:
                        return False

        def directionAlgorithm(hitNull, hitOne, direction):
            if direction == "horizontal+":
                if hitOne + 1 == 10:
                    if self.battleMap[hitNullNull][hitOneOne - 1] == "[ ]" or self.battleMap[hitNullNull][
                        hitOneOne - 1] == "[*]":
                        # проверяет уничтожен корабль или нет
                        print("Бот уничтожил твой корабль! ")
                        # передаем в метод для раставления точек
                        dotsAroundShips("x+", hitNullNull, hitOneOne)
                        self.botMemory = ""
                        return True
                    else:
                        self.botMemory = "x+"
                        return False
                if self.battleMap[hitNull][hitOne + 1] != "[*]" or self.battleMap[hitNull][
                    hitOne + 1] != "[x]":
                    if self.battleMap[hitNull][hitOne + 1] == "[O]":
                        self.battleMap[hitNull][hitOne + 1] = "[x]"
                        directionAlgorithm(hitNull, hitOne + 1, "horizontal+")
                        # проходит и уничтожает до конца
                    else:
                        if self.battleMap[hitNullNull][hitOneOne - 1] == "[ ]" or self.battleMap[hitNullNull][
                            hitOneOne - 1] == "[*]" or (hitOneOne - 1) == -1:
                            # проверяет уничтожен корабль или нет
                            print("Бот уничтожил твой корабль! ")
                            # передаем в метод для раставления точек
                            dotsAroundShips("x+", hitNullNull, hitOneOne)
                            self.botMemory = ""
                            return True
                        else:
                            self.battleMap[hitNull][hitOne + 1] = "[*]"
                            self.botMemory = "x-"
                            self.botMemoryCoordinatesNull = hitNullNull
                            self.botMemoryCoordinatesOne = hitOneOne

                            return False
            elif direction == "horizontal-":
                if self.battleMap[hitNull][hitOne - 1] != "[*]" or self.battleMap[hitNull][
                    hitOne - 1] != "[x]" or (hitOne - 1) != -1:
                    if self.battleMap[hitNull][hitOne - 1] == "[O]":
                        self.battleMap[hitNull][hitOne - 1] = "[x]"
                        directionAlgorithm(hitNull, hitOne - 1, "horizontal-")
                        # проходит и уничтожает до конца
                    else:
                        if cheekShoot(hitNull, hitOne, "hitOne+"):
                            self.botMemory = ""
                            return True
                        else:
                            self.battleMap[hitNull][hitOne - 1] = "[*]"
                            self.botMemory = "x+"
                            return False

        def demolitionAlgorithm(hitNull, hitOne):
            # проверяем однопалубный корабль у границы
            if hitOne + 1 == 10:
                # проверяем однопалубный корабль у двух границ
                if hitNull + 1 == 10:
                    if (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
                        hitOne - 1] != "[x]") \
                            and (self.battleMap[hitNull - 1][hitOne] != "[O]" and self.battleMap[hitNull - 1][
                        hitOne] != "[x]"):
                        if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
                            self.botMemory = ""
                            return True
                # проверяем однопалубный корабль у двух границ
                if hitNull - 1 == -1:
                    if (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
                        hitOne - 1] != "[x]") \
                            and (self.battleMap[hitNull + 1][hitOne] != "[O]" and self.battleMap[hitNull + 1][
                        hitOne] != "[x]"):
                        if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
                            self.botMemory = ""
                            return True
                # проверяем однопалубный корабль у границы
                if (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
                    hitOne - 1] != "[x]") \
                        and (self.battleMap[hitNull - 1][hitOne] != "[O]" and self.battleMap[hitNull - 1][
                    hitOne] != "[x]") \
                        and (self.battleMap[hitNull + 1][hitOne] != "[O]" and self.battleMap[hitNull + 1][
                    hitOne] != "[x]"):
                    if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
                        self.botMemory = ""
                        return True

            # проверяем направление в x- прижата к границе
            if (hitOne + 1) == 10:
                if (self.battleMap[hitNull][hitOne - 1] != "[*]" or self.battleMap[hitNull][
                    hitOne - 1] != "[x]") \
                        and (self.botMemory == "x-" or self.botMemory == ""):
                    if self.battleMap[hitNull][hitOne - 1] == "[O]":
                        self.battleMap[hitNull][hitOne - 1] = "[x]"
                        # направление подтвердилось проверяем дальше
                        if directionAlgorithm(hitNull, hitOne - 1, "horizontal-") == True:
                            return True

                    else:
                        self.battleMap[hitNull][hitOne - 1] = "[*]"
                        self.botMemoryCoordinatesNull = hitNull
                        self.botMemoryCoordinatesOne = hitOne
                        return False

            # проверяем направление в x+ прижата к границе
            if hitOne - 1 == -1:
                if (self.battleMap[hitNull][hitOne + 1] != "[*]" or self.battleMap[hitNull][hitOne + 1] != "[x]") \
                        and (self.botMemory == "x+" or self.botMemory == ""):
                    if self.battleMap[hitNull][hitOne + 1] == "[O]":
                        self.battleMap[hitNull][hitOne + 1] = "[x]"
                        # направление подтвердилось проверяем дальше
                        if directionAlgorithm(hitNull, hitOne + 1, "horizontal+") == True:
                            return True

                    else:
                        self.battleMap[hitNull][hitOne + 1] = "[*]"
                        self.botMemoryCoordinatesNull = hitNull
                        self.botMemoryCoordinatesOne = hitOne
                        return False

            # проверяем однопалубный корабль в поле
            elif (self.battleMap[hitNull][hitOne + 1] != "[O]" and self.battleMap[hitNull][
                hitOne + 1] != "[x]") \
                    and (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
                hitOne - 1] != "[x]") \
                    and (self.battleMap[hitNull + 1][hitOne] != "[O]" and self.battleMap[hitNull + 1][
                hitOne] != "[x]") \
                    and (self.battleMap[hitNull - 1][hitOne] != "[O]" and self.battleMap[hitNull - 1][
                hitOne] != "[x]"):
                if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
                    self.botMemory = ""
                    return True
            # проверяем направление в x+
            elif (self.battleMap[hitNull][hitOne + 1] != "[*]" or self.battleMap[hitNull][hitOne + 1] != "[x]") \
                    and (self.botMemory == "x+" or self.botMemory == ""):
                directionAlgorithm(hitNull, hitOne, "horizontal+")
            # проверяем направление в x-
            elif (self.battleMap[hitNull][hitOne - 1] != "[*]" or self.battleMap[hitNull][
                hitOne - 1] != "[x]") \
                    and (self.botMemory == "x-" or self.botMemory == ""):
                directionAlgorithm(hitNull, hitOne, "horizontal-")

        if self.botMemory != "":
            if self.botMemory == "x+":
                hitNull = self.botMemoryCoordinatesNull
                hitOne = self.botMemoryCoordinatesOne
            if self.botMemory == "x-":
                hitNull = self.botMemoryCoordinatesNull
                hitOne = self.botMemoryCoordinatesOne - 1
        else:
            # выбор рандомного координата
            try:
                hitNull = random.randint(0, 9)
                hitOne = random.randint(0, 9)

            except Exception:
                hitNull = 0
                hitOne = 0
                if self.battleMap[hitNull][hitOne] != "[ ]" or self.battleMap[hitNull][hitOne] != "[O]":
                    for i in range(10):
                        if self.battleMap[hitNull][hitOne] == "[ ]" or self.battleMap[hitNull][hitOne] == "[O]":
                            hitOne = i
                            break
                        else:
                            for q in range(10):
                                for i1 in range(10):
                                    if self.battleMap[q][i1] == "[ ]" or self.battleMap[q][i1] == "[O]":
                                        hitNull = q
                                        hitOne = i1
                                        break
                            print("Игра окончина! ")

        if self.battleMap[hitNull][hitOne] == "[ ]":
            self.battleMap[hitNull][hitOne] = "[*]"
            print("Бот промазал !")
            time.sleep(3)
            return False
            # промазал
        else:
            if self.battleMap[hitNull][hitOne] == "[*]" or self.battleMap[hitNull][hitOne] == "[x]":
                self.artificialIntelligence()
                # не трогать
            else:
                # попал
                self.battleMap[hitNull][hitOne] = "[x]"
                print("Бот попал !")
                time.sleep(3)
                # обозначить
                hitNullNull = hitNull
                hitOneOne = hitOne
                # передать для определения направления
                if demolitionAlgorithm(hitNull, hitOne):
                    self.artificialIntelligence()
                else:
                    return False

    def start_game(self):
        print("Добропожаловать в")
        print(
            "------------------------------------------------------------МОРСКОЙ БОЙ------------------------------------------------------------")
        time.sleep(5)
        print("\nДавайте начнем игру!")
        time.sleep(1)
        self.creatingShipsAutomatically(self.battleMapBot)
        print("\nКак вы хотите создать карту?")
        self.methodSelection()
        time.sleep(4)
        print("\n\n\n\n\n\n")
        print("\nБот готов надрать вам задницу "
              "\nТак давайте же приступим к сражению!!!!!!!!!!!!!!")
        time.sleep(2)
        print("\n\nДля выхода введите 'end'")
        time.sleep(2)
        print("\n\n\n\n\n\n\n")

        while True:
            for i in range(10):
                print(self.battleMapBot_view[i])
            print("\nВведите кординаты для пушечного залпа:\n ")
            enter_user = input().split()
            if enter_user[0] == "end":
                break
            if len(enter_user) != 2 or (int(enter_user[0]) < 1 or int(enter_user[0]) > 10) \
                    or (int(enter_user[1]) < 1 or int(enter_user[1]) > 10):
                print("Вы ввели неверные координаты! Попробуйте еще раз:\n")
                continue
            row = int(enter_user[0])
            col = int(enter_user[1])
            if self.shoot(row - 1, col - 1):
                print("\n")
                for i in range(10):
                    print(self.battleMapBot_view[i])
                continue
            print("Теперь атакует Бот")
            print("\n\n\n\n\n\n")
            time.sleep(1)
            self.artificialIntelligence()
            for i in range(10):
                print(self.battleMap[i])
            time.sleep(4)
            print("Ваш ход!"+"\n")



a = SeaMap()
a.start_game()
