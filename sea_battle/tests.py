# #import sea_battle_map
# import random
# import time
#
#
# class SeaMap:
#
#     def __init__(self):#, gameMap):
#         self.battleMap = [["[ ]"] * 10 for i in range(10)]
#         self.battleMapBot = [["[ ]"] * 10 for i in range(10)]
#         self.battleMapBot_view = [["[ ]"] * 10 for i in range(10)]
#         self.botMemory = ""
#         self.botMemoryCoordinatesNull = 0
#         self.botMemoryCoordinatesOne = 0
#         #self.gameMapOne = gameMap
#
#     def shoot(self, row, col):#, self_game_map):
#         def dotsAroundShips(tapy, tapyNullX, tapyOneX, one, two):
#             if tapy == "x+":
#                 if self.battleMapBot[tapyNullX][tapyOneX] != "[O]" or self.battleMapBot[tapyNullX][
#                     tapyOneX] != "[x]":
#                     if tapyOneX - 1 != -1:
#                         if tapyNullX - 1 != -1:
#                             self.battleMapBot[tapyNullX - 1][tapyOneX - 1] = "[*]"
#                             self.battleMapBot_view[tapyNullX - 1][tapyOneX - 1] = "[*]"
#
#                         if tapyNullX + 1 != 10:
#                             self.battleMapBot[tapyNullX + 1][tapyOneX - 1] = "[*]"
#                             self.battleMapBot_view[tapyNullX + 1][tapyOneX - 1] = "[*]"
#
#                         self.battleMapBot[tapyNullX][tapyOneX - 1] = "[*]"
#                         self.battleMapBot_view[tapyNullX][tapyOneX - 1] = "[*]"
#
#                     if self.battleMapBot[tapyNullX][tapyOneX] == "[x]":
#                         if tapyNullX - 1 != -1:
#                             self.battleMapBot[tapyNullX - 1][tapyOneX] = "[*]"
#                             self.battleMapBot_view[tapyNullX - 1][tapyOneX] = "[*]"
#
#                         if tapyNullX + 1 != 10:
#                             self.battleMapBot[tapyNullX + 1][tapyOneX] = "[*]"
#                             self.battleMapBot_view[tapyNullX + 1][tapyOneX] = "[*]"
#
#                         if tapyOneX + 1 != 10:
#                             if self.battleMapBot[tapyNullX][tapyOneX + 1] == "[x]":
#                                 if tapyNullX - 1 != -1:
#                                     self.battleMapBot[tapyNullX - 1][tapyOneX + 1] = "[*]"
#                                     self.battleMapBot_view[tapyNullX - 1][tapyOneX + 1] = "[*]"
#
#                                 if tapyNullX + 1 != 10:
#                                     self.battleMapBot[tapyNullX + 1][tapyOneX + 1] = "[*]"
#                                     self.battleMapBot_view[tapyNullX + 1][tapyOneX + 1] = "[*]"
#
#                                 if tapyOneX + 2 != 10:
#                                     if self.battleMapBot[tapyNullX][tapyOneX + 2] == "[x]":
#                                         if tapyNullX - 1 != -1:
#                                             self.battleMapBot[tapyNullX - 1][tapyOneX + 2] = "[*]"
#                                             self.battleMapBot_view[tapyNullX - 1][tapyOneX + 2] = "[*]"
#
#                                         if tapyNullX + 1 != 10:
#                                             self.battleMapBot[tapyNullX + 1][tapyOneX + 2] = "[*]"
#                                             self.battleMapBot_view[tapyNullX + 1][tapyOneX + 2] = "[*]"
#
#                                         if tapyOneX + 3 != 10:
#                                             if self.battleMapBot[tapyNullX][tapyOneX + 3] == "[x]":
#                                                 if tapyNullX - 1 != -1:
#                                                     self.battleMapBot[tapyNullX - 1][tapyOneX + 3] = "[*]"
#                                                     self.battleMapBot_view[tapyNullX - 1][tapyOneX + 3] = "[*]"
#
#                                                 if tapyNullX + 1 != 10:
#                                                     self.battleMapBot[tapyNullX + 1][tapyOneX + 3] = "[*]"
#                                                     self.battleMapBot_view[tapyNullX + 1][tapyOneX + 3] = "[*]"
#
#                                                 if tapyOneX + 4 != 10:
#                                                     if tapyNullX - 1 != -1:
#                                                         self.battleMapBot[tapyNullX - 1][tapyOneX + 4] = "[*]"
#                                                         self.battleMapBot_view[tapyNullX - 1][tapyOneX + 4] = "[*]"
#
#                                                     if tapyNullX + 1 != 10:
#                                                         self.battleMapBot[tapyNullX + 1][tapyOneX + 4] = "[*]"
#                                                         self.battleMapBot_view[tapyNullX + 1][tapyOneX + 4] = "[*]"
#
#                                                     self.battleMapBot[tapyNullX][tapyOneX + 4] = "[*]"
#                                                     self.battleMapBot_view[tapyNullX][tapyOneX + 4] = "[*]"
#
#                                             else:
#                                                 if tapyNullX - 1 != -1:
#                                                     self.battleMapBot[tapyNullX - 1][tapyOneX + 3] = "[*]"
#                                                     self.battleMapBot_view[tapyNullX - 1][tapyOneX + 3] = "[*]"
#
#                                                 if tapyNullX + 1 != 10:
#                                                     self.battleMapBot[tapyNullX + 1][tapyOneX + 3] = "[*]"
#                                                     self.battleMapBot_view[tapyNullX + 1][tapyOneX + 3] = "[*]"
#
#                                                 self.battleMapBot[tapyNullX][tapyOneX + 3] = "[*]"
#                                                 self.battleMapBot_view[tapyNullX][tapyOneX + 3] = "[*]"
#
#                                     else:
#                                         if tapyNullX - 1 != -1:
#                                             self.battleMapBot[tapyNullX - 1][tapyOneX + 2] = "[*]"
#                                             self.battleMapBot_view[tapyNullX - 1][tapyOneX + 2] = "[*]"
#
#                                         if tapyNullX + 1 != 10:
#                                             self.battleMapBot[tapyNullX + 1][tapyOneX + 2] = "[*]"
#                                             self.battleMapBot_view[tapyNullX + 1][tapyOneX + 2] = "[*]"
#
#                                         self.battleMapBot[tapyNullX][tapyOneX + 2] = "[*]"
#                                         self.battleMapBot_view[tapyNullX][tapyOneX + 2] = "[*]"
#
#
#                             else:
#                                 if tapyNullX - 1 != -1:
#                                     if tapyOneX + 1 != 10:
#                                         self.battleMapBot[tapyNullX - 1][tapyOneX + 1] = "[*]"
#                                         self.battleMapBot_view[tapyNullX - 1][tapyOneX + 1] = "[*]"
#
#                                 if tapyNullX + 1 != 10:
#                                     if tapyOneX + 1 != 10:
#                                         self.battleMapBot[tapyNullX + 1][tapyOneX + 1] = "[*]"
#                                         self.battleMapBot_view[tapyNullX + 1][tapyOneX + 1] = "[*]"
#                                         print("*")
#                                 if tapyOneX + 1 != 10:
#                                     self.battleMapBot[tapyNullX][tapyOneX + 1] = "[*]"
#                                     self.battleMapBot_view[tapyNullX][tapyOneX + 1] = "[*]"
#                                     print("*")
#
#         def cheekShoot(hitNull, hitOne):
#             #one = int(self_game_map.objectName()[13])
#             #two = int(self_game_map.objectName()[14])
#             # ?????????????????? ???????????????????????? ?????????????? ?? ??????????????
#             if hitOne + 1 == 10:
#                 # ?????????????????? ???????????????????????? ?????????????? ?? ???????? ????????????
#                 if hitNull + 1 == 10:
#                     if (self.battleMapBot[hitNull][hitOne - 1] != "[O]" and self.battleMapBot[hitNull][
#                         hitOne - 1] != "[x]") \
#                             and (self.battleMapBot[hitNull - 1][hitOne] != "[O]" and self.battleMapBot[hitNull - 1][
#                         hitOne] != "[x]"):
#                         # ???????????????????? ?? ??????????
#                         print("???? ???????????????????? ??????????????!")
#                         dotsAroundShips("x+", hitNull, hitOne, one, two)
#                 # ?????????????????? ???????????????????????? ?????????????? ?? ???????? ????????????
#                 if hitNull - 1 == -1:
#                     if (self.battleMapBot[hitNull][hitOne - 1] != "[O]" and self.battleMapBot[hitNull][
#                         hitOne - 1] != "[x]") \
#                             and (self.battleMapBot[hitNull + 1][hitOne] != "[O]" and self.battleMapBot[hitNull + 1][
#                         hitOne] != "[x]"):
#                         # ???????????????????? ?? ??????????
#                         print("???? ???????????????????? ??????????????!")
#                         dotsAroundShips("x+", hitNull, hitOne, one, two)
#                 # ?????????????????? ???????????????????????? ?????????????? ?? ??????????????
#                 if (self.battleMapBot[hitNull][hitOne - 1] != "[O]" and self.battleMapBot[hitNull][
#                     hitOne - 1] != "[x]") \
#                         and (self.battleMapBot[hitNull - 1][hitOne] != "[O]" and self.battleMapBot[hitNull - 1][
#                     hitOne] != "[x]") \
#                         and (self.battleMapBot[hitNull + 1][hitOne] != "[O]" and self.battleMapBot[hitNull + 1][
#                     hitOne] != "[x]"):
#                     # ???????????????????? ?? ??????????
#                     print("???? ???????????????????? ??????????????!")
#                     dotsAroundShips("x+", hitNull, hitOne, one, two)
#
#             # ?????????????????? ???????????????????????? ?????????????? ?? ????????
#             elif hitOne + 1 != 10 and hitOne - 1 != -1:
#                 if hitNull + 1 != 10 and hitNull - 1 != -1:
#                     if (self.battleMapBot[hitNull][hitOne + 1] != "[O]" and self.battleMapBot[hitNull][
#                         hitOne + 1] != "[x]") \
#                             and (self.battleMapBot[hitNull][hitOne - 1] != "[O]" and self.battleMapBot[hitNull][
#                         hitOne - 1] != "[x]") \
#                             and (self.battleMapBot[hitNull + 1][hitOne] != "[O]" and self.battleMapBot[hitNull + 1][
#                         hitOne] != "[x]") \
#                             and (self.battleMapBot[hitNull - 1][hitOne] != "[O]" and self.battleMapBot[hitNull - 1][
#                         hitOne] != "[x]"):
#                         # ???????????????????? ?? ??????????
#                         print("???? ???????????????????? ??????????????!")
#                         dotsAroundShips("x+", hitNull, hitOne, one, two)
#
#             # ?????????????????? ?????????????? ???? 1 ???? 4 ??????????
#             for i in range(1, 5):
#                 result = False
#                 if hitOne + 1 == 10:
#                     for i1 in range(1, 5):
#                         if self.battleMapBot[hitNull][hitOne - i1] == "[*]" \
#                                 or self.battleMapBot[hitNull][hitOne - i1] == "[ ]":
#                             # ???????????????????? ?? ??????????
#                             print(111111111111)
#                             print("???? ???????????????????? ??????????????!")
#
#                             dotsAroundShips("x+", hitNull, hitOne - i1 + 1, one, two - i1 + 1)
#                             result = True
#                             break
#                         elif self.battleMapBot[hitNull][hitOne - i1] == "[O]":
#                             result = True
#                             break
#                 elif self.battleMapBot[hitNull][hitOne + i] == "[*]" \
#                         or self.battleMapBot[hitNull][hitOne + i] == "[ ]":
#                     for i1 in range(1, 5):
#                         if hitOne - 1 == -1:
#                             # ???????????????????? ?? ??????????
#                             print(2222222222)
#                             print("???? ???????????????????? ??????????????!")
#                             dotsAroundShips("x+", hitNull, hitOne , one, two - i1)
#                             result = True
#                             break
#                         elif self.battleMapBot[hitNull][hitOne - i1] == "[*]" \
#                                 or self.battleMapBot[hitNull][hitOne - i1] == "[ ]":
#                             # ???????????????????? ?? ??????????
#                             print(333333333)
#                             print("???? ???????????????????? ??????????????!")
#                             dotsAroundShips("x+", hitNull, hitOne - i1 + 1, one, two - i1 + 1)
#                             result = True
#                             break
#                         elif self.battleMapBot[hitNull][hitOne - i1] == "[O]":
#                             result = True
#                             break
#                 elif self.battleMapBot[hitNull][hitOne + i] == "[O]":
#                     break
#                 if result == True:
#                     break
#
#         check = self.battleMapBot[row][col]
#         if check == "[x]" or check == "[*]":
#             print("???? ???????? ????????????????! ???????????????????? ?????? ??????...")
#         elif check == "[O]":
#             self.battleMapBot[row][col] = "[x]"
#             self.battleMapBot_view[row][col] = "[x]"
#             cheekShoot(row, col)
#         else:
#             self.battleMapBot[row][col] = "[*]"
#             self.battleMapBot_view[row][col] = "[*]"
#             #self.artificialIntelligence()
#
#     def methodSelection(self):
#         print("???????? ?? ???????????? ?????????????? '1' ")
#         print("???????? ?????????????????????????? ?????????????? '2'\n: ")
#         try:
#             choiceUser = int(input())
#         except Exception:
#             print("???? ?????????? ???????????????? ????????????????! ")
#             print("???????????????????? ?????? ??????")
#             self.methodSelection()
#         if choiceUser == 1:
#             self.creatingShipsMechanically()
#         elif choiceUser == 2:
#             self.creatingShipsAutomatically(self.battleMapBot)
#             print("?????????? ?????????????? !")
#             print("\n?????? ?????????? ?????????????? ?????? ?????????????? "
#                   "\n?????? ?????????????? ???? ?????????????????? ?? ????????????????!!!!!!!!!!!!!!")
#
#         else:
#             print("???? ?????????? ???????????????? ????????????????! ")
#             print("???????????????????? ?????? ??????")
#             self.methodSelection()
#
#     def creatingShipsMechanically(self):
#         def shipsNearbyHorizontal(player, row, col, decks):
#             if player.battleMap[row][col] != "[O]" and player.battleMap[row][col - decks] != "[O]":
#                 for i in range(decks + 1):
#                     if player.battleMap[row - 1][(col) - i] == "[O]":
#                         return False
#                     if player.battleMap[row + 1][(col) - i] == "[O]":
#                         return False
#                 return True
#
#         def shipsNearbyVertical(player, col, row, decks):
#             if player.battleMap[row][col] != "[O]" and player.battleMap[row - decks][col] != "[O]":
#                 for i in range(decks + 1):
#                     if player.battleMap[row - i][col - 1] == "[O]":
#                         return False
#                     if player.battleMap[row - i][col + 1] == "[O]":
#                         return False
#                 return True
#
#         def creatingShip(player, decks):
#             for i in range(10):
#                 print(self.battleMap[i])
#             print("?????????????? ???????????? ?????????????????? ??????????????: ")
#             start = input().split()
#             startNull = int(start[0])
#             startOne = int(start[1])
#             if (-1 < startNull < 11) and (-1 < startOne < 11):
#                 print("?????????????? ?????????? ?????????????????? ??????????????: ")
#                 end = input().split()
#                 endNull = int(end[0])
#                 endOne = int(end[1])
#                 result = startNull - endNull + startOne - endOne
#                 if (-1 < endNull < 11) and (-1 < endOne < 11) and (result == decks or result == (-decks)):
#                     if startNull == endNull:
#                         if result == -decks:
#                             for q in range(startOne, (startOne) + decks + 1):
#                                 if player.battleMap[startNull - 1][q - 1] == "[O]":
#                                     print("?????? ???????????????????? ????????????! ")
#                                     creatingShip(player, decks)
#                                     break
#                             if shipsNearbyHorizontal(player, startNull - 1, (startOne) + decks, decks + 2):
#                                 for q in range(startOne, (startOne) + decks + 1):
#                                     player.battleMap[startNull - 1][q - 1] = "[O]"
#                             else:
#                                 print("?????????????? ?????????????? ???????????? ?? ?????????????? ! ")
#                                 creatingShip(player, decks)
#
#
#
#                         else:
#                             for q in range(endOne, (endOne) + decks + 1):
#                                 if player.battleMap[startNull - 1][q - 1] == "[O]":
#                                     print("?????? ???????????????????? ????????????! ")
#                                     creatingShip(player, decks)
#                                     break
#                             if shipsNearbyHorizontal(player, endNull - 1, (endOne) + decks, decks + 2):
#                                 for q in range(endOne, (endOne) + decks + 1):
#                                     player.battleMap[startNull - 1][q - 1] = "[O]"
#                             else:
#                                 print("?????????????? ?????????????? ???????????? ?? ?????????????? ! ")
#                                 creatingShip(player, decks)
#
#                     else:
#                         if result == -decks:
#                             for q in range(startNull, startNull + decks + 1):
#                                 if player.battleMap[q - 1][startOne - 1] == "[O]":
#                                     print("?????? ???????????????????? ????????????! ")
#                                     creatingShip(player, decks)
#                                     break
#                             if shipsNearbyVertical(player, startOne - 1, (startNull) + decks, decks + 1):
#                                 for q in range(startNull, startNull + decks + 1):
#                                     player.battleMap[q - 1][startOne - 1] = "[O]"
#                             else:
#                                 print("?????????????? ?????????????? ???????????? ?? ?????????????? ! ")
#                                 creatingShip(player, decks)
#
#                         else:
#                             for q in range(endNull, endNull + decks + 1):
#                                 if player.battleMap[q - 1][startOne - 1] == "[O]":
#                                     print("?????? ???????????????????? ????????????! ")
#                                     creatingShip(player, decks)
#                                     break
#                             if shipsNearbyVertical(player, endOne - 1, (endNull) + decks, decks + 1):
#                                 for q in range(endNull, endNull + decks + 1):
#                                     player.battleMap[q - 1][endOne - 1] = "[O]"
#                             else:
#                                 print("?????????????? ?????????????? ???????????? ?? ?????????????? ! ")
#                                 creatingShip(player, decks)
#
#                 else:
#                     print("???? ?????????????????????? ?????????? ???????????????????? ")
#                     creatingShip(player, decks)
#             else:
#                 print("???? ?????????????????????? ?????????? ???????????????????? ")
#                 creatingShip(player, decks)
#
#         print("?????????? ???????????????????? ???????? ???????????????? ???? ????????:"
#               " 1 - ?????????????? ???????????????? , 1 - ???????? ????????????????, 2 - ???????? ???????????????? ")
#
#         print("???????????? ?? ??????????????-?????????????????? ??????????????")
#         creatingShip(self, 3)
#         print("?????????????????????? ?????? ???????? ??????????????-???????????????? ??????????????")
#         creatingShip(self, 3)
#         print("???????????? ???????????????????? ????????-???????????????? ??????????????")
#         creatingShip(self, 2)
#         print("?????????????????????? ?????? ???????? ????????-???????????????? ??????????????")
#         creatingShip(self, 2)
#         print("???????????? ???????????????????? ????????-???????????????? ??????????????")
#         creatingShip(self, 1)
#         print("?????????????????????? ?????? ???????? ????????-???????????????? ??????????????")
#         creatingShip(self, 1)
#         print("???????????? ???????????????????? ???????? ????????-???????????????? ??????????????")
#         creatingShip(self, 0)
#         for i in range(10):
#             print(self.battleMap[i])
#
#     def creatingShipsAutomatically(self, map):
#         def creatingShip(decks):
#             # ???????????? ?????????????????? ??????????????
#             choice = 2  # random.randint(1, 2)
#             bulin??heck = True
#             startNull = random.randint(1, 10)
#             startOne = random.randint(1, 10)
#             if choice == 1:
#                 # ?????????? ?????????????????? ??????????????
#                 if startNull + decks < 11 and (decks == 3 or decks == 2 or decks == 1 or decks == 0):
#                     for q in range(decks + 3):
#                         try:
#                             if map[startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][
#                                 startOne - 1] == "[O]" \
#                                     or map[
#                                 startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][
#                                 startOne - 2 if startOne - 2 != -1 else startOne - 1] == "[O]" \
#                                     or map[
#                                 startNull - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q][startOne] == "[O]":
#                                 bulin??heck = False
#                                 creatingShip(decks)
#                                 break
#                         except Exception:
#                             pass
#                     if bulin??heck:
#                         for q in range(decks + 1):
#                             map[startNull - 1 + q][startOne - 1] = "[O]"
#
#                 elif startNull + decks > 0 and (decks == -3 or decks == -2 or decks == -1):
#                     for q in range((-decks) + 3):
#                         try:
#                             if map[startNull - q if startNull - q != -1 else startNull - q + 1][
#                                 startOne - 1] == "[O]" \
#                                     or map[startNull - q if startNull - q != -1 else startNull - q + 1][
#                                 startOne - 2 if startOne - 2 != -1 else startOne - 1] == "[O]" \
#                                     or map[startNull - q if startNull - q != -1 else startNull - q + 1][
#                                 startOne] == "[O]":
#                                 bulin??heck = False
#                                 creatingShip(decks)
#                                 break
#                         except Exception:
#                             pass
#                     if bulin??heck:
#                         for q in range((-decks) + 1):
#                             map[(startNull - 1) - q][startOne - 1] = "[O]"
#                 else:
#                     creatingShip(decks)
#             else:
#                 if startOne + decks < 10 and (decks == 3 or decks == 2 or decks == 1 or decks == 0):  # ?????????? ??????
#
#                     for q in range(decks + 3):
#                         try:
#                             if map[startNull - 1][
#                                 startOne - 2 + q if startNull - 2 + q != -1 else startNull - 1 + q] == "[O]" \
#                                     or map[startNull - 2 if startNull - 2 != -1 else startNull - 1][
#                                 startOne - 2 + q if startOne - 2 + q != -1 else startOne - 1 + q] == "[O]" \
#                                     or map[startNull if startNull != -1 else startNull + 1][
#                                 startOne - 2 + q if startOne - 2 + q != -1 else startOne - 1 + q] == "[O]":
#                                 bulin??heck = False
#                                 creatingShip(decks)
#                                 break
#                         except Exception:
#                             pass
#                     if bulin??heck:
#                         for q in range(decks + 1):
#                             map[startNull - 1][startOne - 1 + q] = "[O]"
#
#                 elif startOne + decks > 0 and (decks == -3 or decks == -2 or decks == -1 or decks == 0):
#
#                     for q in range((-decks) + 3):
#                         try:
#                             if map[startNull - 1][
#                                 startOne - q if startNull - q != -1 else startNull - 1 - q] == "[O]" \
#                                     or map[startNull - 2 if startNull - 2 != -1 else startNull - 1][
#                                 startOne - q if startOne - q != -1 else startOne - 1 - q] == "[O]" \
#                                     or map[startNull if startNull != -1 else startNull - 1][
#                                 startOne - q if startOne - q != -1 else startOne - 1 - q] == "[O]":
#                                 bulin??heck = False
#                                 creatingShip(decks)
#                                 break
#                         except Exception:
#                             pass
#                     if bulin??heck:
#                         for q in range((-decks) + 1):
#                             map[startNull - 1][startOne - 1 - q] = "[O]"
#                 else:
#                     creatingShip(decks)
#
#         creatingShip(random.choice([-3, 3]))
#         creatingShip(random.choice([-3, 3]))
#         creatingShip(random.choice([-2, 2]))
#         creatingShip(random.choice([-2, 2]))
#         creatingShip(random.choice([-1, 1]))
#         creatingShip(random.choice([-1, 1]))
#         creatingShip(0)
#         creatingShip(0)
#         creatingShip(0)
#
#     #def artificialIntelligence(self):
#         # hitNullNull = 0
#         # hitOneOne = 0
#         #
#         # def button_processing(one, two):
#         #     button_name = "pushButton" + str(one) + str(two)
#         #     button = getattr(self.gameMapOne, button_name)
#         #     button.setText("*")
#         #
#         # def button_processing??(one, two):
#         #     button_name = "pushButton" + str(one) + str(two)
#         #     button = getattr(self.gameMapOne, button_name)
#         #     button.setText("??")
#         #
#         # def dotsAroundShips(tapy, tapyNullX, tapyOneX):
#         #     if tapy == "x+":
#         #         if self.battleMap[tapyNullX][tapyOneX] != "[O]" or self.battleMap[hitNull][
#         #             hitOne] != "[x]":
#         #             if tapyOneX - 1 != -1:
#         #                 if tapyNullX - 1 != -1:
#         #                     self.battleMap[tapyNullX - 1][tapyOneX - 1] = "[*]"
#         #                     button_processing(tapyNullX-1,tapyOneX-1)
#         #                 if tapyNullX + 1 != 10:
#         #                     self.battleMap[tapyNullX + 1][tapyOneX - 1] = "[*]"
#         #                     button_processing(tapyNullX + 1, tapyOneX - 1)
#         #                 self.battleMap[tapyNullX][tapyOneX - 1] = "[*]"
#         #                 button_processing(tapyNullX, tapyOneX - 1)
#         #             if self.battleMap[tapyNullX][tapyOneX] == "[x]":
#         #                 if tapyNullX - 1 != -1:
#         #                     self.battleMap[tapyNullX - 1][tapyOneX] = "[*]"
#         #                     button_processing(tapyNullX - 1, tapyOneX)
#         #                 if tapyNullX + 1 != 10:
#         #                     self.battleMap[tapyNullX + 1][tapyOneX] = "[*]"
#         #                     button_processing(tapyNullX + 1, tapyOneX)
#         #                 if tapyOneX + 1 != 10:
#         #                     if self.battleMap[tapyNullX][tapyOneX + 1] == "[x]":
#         #                         if tapyNullX - 1 != -1:
#         #                             self.battleMap[tapyNullX - 1][tapyOneX + 1] = "[*]"
#         #                             button_processing(tapyNullX - 1, tapyOneX + 1)
#         #                         if tapyNullX + 1 != 10:
#         #                             self.battleMap[tapyNullX + 1][tapyOneX + 1] = "[*]"
#         #                             button_processing(tapyNullX + 1, tapyOneX + 1)
#         #                         if tapyOneX + 2 != 10:
#         #                             if self.battleMap[tapyNullX][tapyOneX + 2] == "[x]":
#         #                                 if tapyNullX - 1 != -1:
#         #                                     self.battleMap[tapyNullX - 1][tapyOneX + 2] = "[*]"
#         #                                     button_processing(tapyNullX - 1, tapyOneX + 2)
#         #                                 if tapyNullX + 1 != 10:
#         #                                     self.battleMap[tapyNullX + 1][tapyOneX + 2] = "[*]"
#         #                                     button_processing(tapyNullX + 1, tapyOneX + 2)
#         #                                 if tapyOneX + 3 != 10:
#         #                                     if self.battleMap[tapyNullX][tapyOneX + 3] == "[x]":
#         #                                         if tapyNullX - 1 != -1:
#         #                                             self.battleMap[tapyNullX - 1][tapyOneX + 3] = "[*]"
#         #                                             button_processing(tapyNullX - 1, tapyOneX + 3)
#         #                                         if tapyNullX + 1 != 10:
#         #                                             self.battleMap[tapyNullX + 1][tapyOneX + 3] = "[*]"
#         #                                             button_processing(tapyNullX + 1, tapyOneX + 3)
#         #                                         if tapyOneX + 4 != 10:
#         #                                             if tapyNullX - 1 != -1:
#         #                                                 self.battleMap[tapyNullX - 1][tapyOneX + 4] = "[*]"
#         #                                                 button_processing(tapyNullX - 1, tapyOneX + 4)
#         #                                             if tapyNullX + 1 != 10:
#         #                                                 self.battleMap[tapyNullX + 1][tapyOneX + 4] = "[*]"
#         #                                                 button_processing(tapyNullX + 1, tapyOneX + 4)
#         #                                             self.battleMap[tapyNullX][tapyOneX + 4] = "[*]"
#         #                                             button_processing(tapyNullX , tapyOneX + 4)
#         #                                     else:
#         #                                         if tapyNullX - 1 != -1:
#         #                                             self.battleMap[tapyNullX - 1][tapyOneX + 3] = "[*]"
#         #                                             button_processing(tapyNullX - 1, tapyOneX + 3)
#         #                                         if tapyNullX + 1 != 10:
#         #                                             self.battleMap[tapyNullX + 1][tapyOneX + 3] = "[*]"
#         #                                             button_processing(tapyNullX + 1, tapyOneX + 3)
#         #                                         self.battleMap[tapyNullX][tapyOneX + 3] = "[*]"
#         #                                         button_processing(tapyNullX , tapyOneX + 3)
#         #                             else:
#         #
#         #                                 if tapyNullX - 1 != -1:
#         #                                     self.battleMap[tapyNullX - 1][tapyOneX + 2] = "[*]"
#         #                                     button_processing(tapyNullX - 1, tapyOneX + 2)
#         #                                 if tapyNullX + 1 != 10:
#         #                                     self.battleMap[tapyNullX + 1][tapyOneX + 2] = "[*]"
#         #                                     button_processing(tapyNullX + 1, tapyOneX + 2)
#         #                                 self.battleMap[tapyNullX][tapyOneX + 2] = "[*]"
#         #                                 button_processing(tapyNullX, tapyOneX + 2)
#         #
#         #                     else:
#         #                         if tapyNullX - 1 != -1:
#         #                             if tapyOneX + 1 != 10:
#         #                                 self.battleMap[tapyNullX - 1][tapyOneX + 1] = "[*]"
#         #                                 button_processing(tapyNullX - 1, tapyOneX + 1)
#         #                         if tapyNullX + 1 != 10:
#         #                             if tapyOneX + 1 != 10:
#         #                                 self.battleMap[tapyNullX + 1][tapyOneX + 1] = "[*]"
#         #                                 button_processing(tapyNullX + 1, tapyOneX + 1)
#         #                         if tapyOneX + 1 != 10:
#         #                             self.battleMap[tapyNullX][tapyOneX + 1] = "[*]"
#         #                             button_processing(tapyNullX , tapyOneX + 1)
#         #
#         # def cheekShoot(hitNull, hitOne, tapy):
#         #     # ?????????????????? ?????????????????? ?????????????? ?????? ??????
#         #
#         #     if tapy == "hitOne+":
#         #         if self.battleMap[hitNull][hitOne + 1] == "[x]":
#         #             if self.battleMap[hitNull][hitOne + 2] == "[x]":
#         #                 if hitOne + 3 != 10:
#         #                     if self.battleMap[hitNull][hitOne + 3] == "[x]":
#         #                         if hitOne + 4 == 10:
#         #                             self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #                             # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                             dotsAroundShips("x+", hitNull, hitOne)
#         #                             self.botMemory = ""
#         #                             return True
#         #                         elif self.battleMap[hitNull][hitOne + 4] == "[*]" or self.battleMap[hitNull][
#         #                             hitOne + 4] == "[ ]":
#         #                             self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #                             # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                             dotsAroundShips("x+", hitNull, hitOne)
#         #                             self.botMemory = ""
#         #                             return True
#         #                         else:
#         #                             return False
#         #                     else:
#         #                         if self.battleMap[hitNull][hitOne + 3] == "[x]" or self.battleMap[hitNull][
#         #                             hitOne + 3] == "[ ]" or self.battleMap[hitNull][hitOne + 3] == "[*]" or (
#         #                                 hitOne + 3) == 10:
#         #                             self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #                             # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                             dotsAroundShips("x+", hitNull, hitOne)
#         #                             self.botMemory = ""
#         #                             return True
#         #                         else:
#         #                             return False
#         #                 else:
#         #                     self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #                     # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                     dotsAroundShips("x+", hitNull, hitOne)
#         #                     self.botMemory = ""
#         #                     return True
#         #             else:
#         #                 if self.battleMap[hitNull][hitOne + 2] == "[x]" or self.battleMap[hitNull][
#         #                     hitOne + 2] == "[ ]" or self.battleMap[hitNull][hitOne + 2] == "[*]" or (
#         #                         hitOne + 2) == 10:
#         #                     self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #                     # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                     dotsAroundShips("x+", hitNull, hitOne)
#         #                     self.botMemory = ""
#         #                     return True
#         #                 else:
#         #                     return False
#         #         else:
#         #             if self.battleMap[hitNull][hitOne + 1] == "[x]" or self.battleMap[hitNull][
#         #                 hitOne + 1] == "[*]" or self.battleMap[hitNull][
#         #                 hitOne + 1] == "[ ]" or (hitOne + 1) == 10:
#         #                 self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #                 # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                 dotsAroundShips("x+", hitNull, hitOne)
#         #                 self.botMemory = ""
#         #                 return True
#         #             else:
#         #                 return False
#         #
#         # def directionAlgorithm(hitNull, hitOne, direction):
#         #     if direction == "horizontal+":
#         #         if hitOne + 1 == 10:
#         #             if self.battleMap[hitNullNull][hitOneOne - 1] == "[ ]" or self.battleMap[hitNullNull][
#         #                 hitOneOne - 1] == "[*]":
#         #                 # ?????????????????? ?????????????????? ?????????????? ?????? ??????
#         #                 self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #                 # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                 dotsAroundShips("x+", hitNullNull, hitOneOne)
#         #                 self.botMemory = ""
#         #                 return True
#         #             else:
#         #                 self.botMemory = "x+"
#         #                 return False
#         #         if self.battleMap[hitNull][hitOne + 1] != "[*]" or self.battleMap[hitNull][
#         #             hitOne + 1] != "[x]":
#         #             if self.battleMap[hitNull][hitOne + 1] == "[O]":
#         #                 #time.sleep(1)
#         #                 self.gameMapOne.label.setText("?????? ?????????? !")
#         #                 self.battleMap[hitNull][hitOne + 1] = "[x]"
#         #                 button_processing??(hitNull, hitOne + 1)
#         #                 directionAlgorithm(hitNull, hitOne + 1, "horizontal+")
#         #                 # ???????????????? ?? ???????????????????? ???? ??????????
#         #             else:
#         #                 if self.battleMap[hitNullNull][hitOneOne - 1] == "[ ]" or self.battleMap[hitNullNull][
#         #                     hitOneOne - 1] == "[*]" or (hitOneOne - 1) == -1:
#         #                     # ?????????????????? ?????????????????? ?????????????? ?????? ??????
#         #
#         #                     self.gameMapOne.label.setText("?????? ?????????????????? ???????? ??????????????! ")
#         #
#         #                     # ???????????????? ?? ?????????? ?????? ?????????????????????? ??????????
#         #                     dotsAroundShips("x+", hitNullNull, hitOneOne)
#         #                     self.botMemory = ""
#         #                     return True
#         #                 else:
#         #                     #time.sleep(1)
#         #
#         #                     self.gameMapOne.label.setText("?????? ???????????????? ! ")
#         #                     self.battleMap[hitNull][hitOne + 1] = "[*]"
#         #                     button_processing(hitNull, hitOne + 1)
#         #                     self.botMemory = "x-"
#         #                     self.botMemoryCoordinatesNull = hitNullNull
#         #                     self.botMemoryCoordinatesOne = hitOneOne
#         #
#         #                     return False
#         #     elif direction == "horizontal-":
#         #         if self.battleMap[hitNull][hitOne - 1] != "[*]" or self.battleMap[hitNull][
#         #             hitOne - 1] != "[x]" or (hitOne - 1) != -1:
#         #             if self.battleMap[hitNull][hitOne - 1] == "[O]":
#         #                 #time.sleep(1)
#         #                 self.gameMapOne.label.setText("?????? ?????????? !")
#         #                 self.battleMap[hitNull][hitOne - 1] = "[x]"
#         #                 button_processing??(hitNull, hitOne - 1)
#         #                 directionAlgorithm(hitNull, hitOne - 1, "horizontal-")
#         #                 # ???????????????? ?? ???????????????????? ???? ??????????
#         #             else:
#         #                 if cheekShoot(hitNull, hitOne, "hitOne+"):
#         #                     self.botMemory = ""
#         #                     return True
#         #                 else:
#         #                     #time.sleep(1)
#         #                     self.gameMapOne.label.setText("?????? ???????????????? ! ")
#         #                     self.battleMap[hitNull][hitOne - 1] = "[*]"
#         #                     button_processing(hitNull, hitOne - 1)
#         #                     self.botMemory = "x+"
#         #                     return False
#         #
#         # def demolitionAlgorithm(hitNull, hitOne):
#         #     # ?????????????????? ???????????????????????? ?????????????? ?? ??????????????
#         #     if hitOne + 1 == 10:
#         #         # ?????????????????? ???????????????????????? ?????????????? ?? ???????? ????????????
#         #         if hitNull + 1 == 10:
#         #             if (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
#         #                 hitOne - 1] != "[x]") \
#         #                     and (self.battleMap[hitNull - 1][hitOne] != "[O]" and self.battleMap[hitNull - 1][
#         #                 hitOne] != "[x]"):
#         #                 if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
#         #                     self.botMemory = ""
#         #                     return True
#         #         # ?????????????????? ???????????????????????? ?????????????? ?? ???????? ????????????
#         #         if hitNull - 1 == -1:
#         #             if (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
#         #                 hitOne - 1] != "[x]") \
#         #                     and (self.battleMap[hitNull + 1][hitOne] != "[O]" and self.battleMap[hitNull + 1][
#         #                 hitOne] != "[x]"):
#         #                 if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
#         #                     self.botMemory = ""
#         #                     return True
#         #         # ?????????????????? ???????????????????????? ?????????????? ?? ??????????????
#         #         if (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
#         #             hitOne - 1] != "[x]") \
#         #                 and (self.battleMap[hitNull - 1][hitOne] != "[O]" and self.battleMap[hitNull - 1][
#         #             hitOne] != "[x]") \
#         #                 and (self.battleMap[hitNull + 1][hitOne] != "[O]" and self.battleMap[hitNull + 1][
#         #             hitOne] != "[x]"):
#         #             if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
#         #                 self.botMemory = ""
#         #                 return True
#         #
#         #     # ?????????????????? ?????????????????????? ?? x- ?????????????? ?? ??????????????
#         #     if (hitOne + 1) == 10:
#         #         if (self.battleMap[hitNull][hitOne - 1] != "[*]" or self.battleMap[hitNull][
#         #             hitOne - 1] != "[x]") \
#         #                 and (self.botMemory == "x-" or self.botMemory == ""):
#         #             if self.battleMap[hitNull][hitOne - 1] == "[O]":
#         #                 #time.sleep(1)
#         #                 self.gameMapOne.label.setText("?????? ?????????? !")
#         #
#         #                 self.battleMap[hitNull][hitOne - 1] = "[x]"
#         #                 button_processing??(hitNull, hitOne - 1)
#         #                 # ?????????????????????? ?????????????????????????? ?????????????????? ????????????
#         #                 if directionAlgorithm(hitNull, hitOne - 1, "horizontal-") == True:
#         #                     return True
#         #
#         #             else:
#         #                 #time.sleep(1)
#         #
#         #                 self.gameMapOne.label.setText("?????? ???????????????? ! ")
#         #                 self.battleMap[hitNull][hitOne - 1] = "[*]"
#         #                 button_processing(hitNull, hitOne - 1)
#         #                 self.botMemoryCoordinatesNull = hitNull
#         #                 self.botMemoryCoordinatesOne = hitOne
#         #                 return False
#         #
#         #     # ?????????????????? ?????????????????????? ?? x+ ?????????????? ?? ??????????????
#         #     if hitOne - 1 == -1:
#         #         if (self.battleMap[hitNull][hitOne + 1] != "[*]" or self.battleMap[hitNull][hitOne + 1] != "[x]") \
#         #                 and (self.botMemory == "x+" or self.botMemory == ""):
#         #             if self.battleMap[hitNull][hitOne + 1] == "[O]":
#         #                 #time.sleep(1)
#         #                 self.gameMapOne.label.setText("?????? ?????????? !")
#         #
#         #                 self.battleMap[hitNull][hitOne + 1] = "[x]"
#         #                 button_processing??(hitNull, hitOne + 1)
#         #                 # ?????????????????????? ?????????????????????????? ?????????????????? ????????????
#         #                 if directionAlgorithm(hitNull, hitOne + 1, "horizontal+") == True:
#         #                     return True
#         #
#         #             else:
#         #                 self.battleMap[hitNull][hitOne + 1] = "[*]"
#         #                 button_processing??(hitNull, hitOne + 1)
#         #                 #time.sleep(1)
#         #
#         #                 self.gameMapOne.label.setText("?????? ???????????????? ! ")
#         #                 self.botMemoryCoordinatesNull = hitNull
#         #                 self.botMemoryCoordinatesOne = hitOne
#         #                 return False
#         #
#         #     # ?????????????????? ???????????????????????? ?????????????? ?? ????????
#         #     if hitOne + 1 != 10 and hitOne - 1 != -1:
#         #         if (self.battleMap[hitNull][hitOne + 1] != "[O]" and self.battleMap[hitNull][
#         #             hitOne + 1] != "[x]") \
#         #                 and (self.battleMap[hitNull][hitOne - 1] != "[O]" and self.battleMap[hitNull][
#         #             hitOne - 1] != "[x]") \
#         #                 and (self.battleMap[hitNull + 1][hitOne] != "[O]" and self.battleMap[hitNull + 1][
#         #             hitOne] != "[x]") \
#         #                 and (self.battleMap[hitNull - 1][hitOne] != "[O]" and self.battleMap[hitNull - 1][
#         #             hitOne] != "[x]"):
#         #             if directionAlgorithm(hitNull, hitOne, "horizontal+") == True:
#         #                 self.botMemory = ""
#         #                 return True
#         #         # ?????????????????? ?????????????????????? ?? x+
#         #         elif (self.battleMap[hitNull][hitOne + 1] != "[*]" or self.battleMap[hitNull][hitOne + 1] != "[x]") \
#         #                 and (self.botMemory == "x+" or self.botMemory == ""):
#         #             directionAlgorithm(hitNull, hitOne, "horizontal+")
#         #         # ?????????????????? ?????????????????????? ?? x-
#         #         elif (self.battleMap[hitNull][hitOne - 1] != "[*]" or self.battleMap[hitNull][
#         #             hitOne - 1] != "[x]") \
#         #                 and (self.botMemory == "x-" or self.botMemory == ""):
#         #             directionAlgorithm(hitNull, hitOne, "horizontal-")
#         #
#         # if self.botMemory != "":
#         #     if self.botMemory == "x+":
#         #         hitNull = self.botMemoryCoordinatesNull
#         #         hitOne = self.botMemoryCoordinatesOne
#         #     if self.botMemory == "x-":
#         #         hitNull = self.botMemoryCoordinatesNull
#         #         hitOne = self.botMemoryCoordinatesOne - 1
#         # else:
#         #     # ?????????? ???????????????????? ????????????????????
#         #     try:
#         #         hitNull = random.randint(0, 9)
#         #         hitOne = random.randint(0, 9)
#         #
#         #     except Exception:
#         #         hitNull = 0
#         #         hitOne = 0
#         #         if self.battleMap[hitNull][hitOne] != "[ ]" or self.battleMap[hitNull][hitOne] != "[O]":
#         #             for i in range(10):
#         #                 if self.battleMap[hitNull][hitOne] == "[ ]" or self.battleMap[hitNull][hitOne] == "[O]":
#         #                     hitOne = i
#         #                     break
#         #                 else:
#         #                     for q in range(10):
#         #                         for i1 in range(10):
#         #                             if self.battleMap[q][i1] == "[ ]" or self.battleMap[q][i1] == "[O]":
#         #                                 hitNull = q
#         #                                 hitOne = i1
#         #                                 break
#         #                     self.gameMapOne.label.setText("???????? ????????????????! ")
#         #
#         # if self.battleMap[hitNull][hitOne] == "[ ]":
#         #     self.battleMap[hitNull][hitOne] = "[*]"
#         #     button_processing(hitNull, hitOne)
#         #     self.gameMapOne.label.setText("?????? ???????????????? !")
#         #     #time.sleep(1)
#         #     return False
#         #     # ????????????????
#         # else:
#         #     if self.battleMap[hitNull][hitOne] == "[*]" or self.battleMap[hitNull][hitOne] == "[x]":
#         #         self.artificialIntelligence()
#         #         # ???? ??????????????
#         #     else:
#         #         # ??????????
#         #         self.battleMap[hitNull][hitOne] = "[x]"
#         #         button_processing??(hitNull, hitOne)
#         #         self.gameMapOne.label.setText("?????? ?????????? !")
#         #         #time.sleep(1)
#         #         # ????????????????????
#         #         hitNullNull = hitNull
#         #         hitOneOne = hitOne
#         #         # ???????????????? ?????? ?????????????????????? ??????????????????????
#         #         if demolitionAlgorithm(hitNull, hitOne):
#         #             self.artificialIntelligence()
#         #         else:
#         #             return False
#
#     def start_game(self):
#         print("?????????????????????????????? ??")
#         print(
#             "------------------------------------------------------------?????????????? ??????------------------------------------------------------------")
#         time.sleep(2)
#         print("\n?????????????? ???????????? ????????!")
#         time.sleep(1)
#         self.creatingShipsAutomatically(self.battleMapBot)
#         print("\n?????? ???? ???????????? ?????????????? ???????????")
#         self.methodSelection()
#
#         # while True:
#         #
#         #
#         #
#         #     if self.shoot(row, col):
#         #         print("\n")
#         #         for i in range(10):
#         #             print(self.battleMapBot_view[i])
#         #         time.sleep(2)
#         #         continue
#         #     print("???????????? ?????????????? ??????")
#         #     print("\n")
#         #     self.artificialIntelligence()
#         #     for i in range(10):
#         #         print(self.battleMap[i])
#         #     time.sleep(4)
#         #     print("?????? ??????!" + "\n")
#
# a = SeaMap()
# # a.methodSelection()
# a.battleMapBot[7][0] = "[O]"
# while True:
#     d = input()
#     one = int(d[0])
#     two = int(d[1])
#     a.shoot(one, two)
#     for i in range(10):
#         print(a.battleMapBot_view[i])
import traceback

try:
    2 / 0
except Exception:
    print(traceback.format_exc())
