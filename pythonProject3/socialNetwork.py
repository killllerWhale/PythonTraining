from abc import ABC, abstractmethod

class Social_Network(ABC):

    def message_user(self, user, message):
        user.new_massages.append(message)

    def message_wall(self, message):
        self.new_massages.append(message)

    @abstractmethod
    def dop_info(self):
        pass

    def printinfo_user(self):
        print("Имя пользователя: " + self.name+" ")
        self.dop_info()

    def get_massages(self):
        while True:
            if len(self.new_massages) > 0:
                print("У вас: " + str(len(self.new_massages)) + " новых сообщений ")
                print("Если хотите просмотреть новые сообщения введите '1' " )
                print("Если хотите выйти введите 'end' ")
                if len(self.massages) > 0:
                    print("Если хотите просмотреть старые сообщения введите '2' ")
                choice = input()
                if choice == "1":
                    for i in range(len(self.new_massages)):
                        print(self.new_massages[i])
                elif choice == "2":
                    for i in range(len(self.massages)):
                        print(self.massages[i])
                elif choice == "end":
                    self.massages.extend(self.new_massages)
                    self.new_massages = []
                    break
                else:
                    print("Вы ввели неверное значение, попробуйте еще раз! ")
            else:
                print("У вас нет новых сообщений! ")
                if len(self.new_massages) > 0:
                    print("Если хотите просмотреть старые сообщения введите '2' ")
                    print("Если хотите выйти введите 'end' ")
                choice = input()
                if choice == "2":
                    for i in range(len(self.massages)):
                        print(self.massages[i])
                elif choice == "end":
                    self.massages.extend(self.new_massages)
                    self.new_massages = []
                    break
                else:
                    print("Вы ввели неверное значение, попробуйте еще раз! ")
                    continue
                print("У вас нет сообщений! ")
                break

class User(Social_Network):

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_birth = date_of_birth
        self.new_massages = []
        self.massages = []
        self.user_subscriptions = []

    def subscription (self, user):
        user.community_subscribers.append(self)
        self.user_subscriptions.append(user)


    def dop_info(self):
        print("Дата рождения: "+ str(self.date_birth))

class Community(Social_Network):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.massages = []
        self.new_massages = []
        self.user_subscriptions = []

    def dop_info(self):
        print("Описание: " + str(self.description))



a = User("Паша", "10.10.2003")
b = User("Маша", "10.10.2003")
a.message_user(b, "Привет")
b.get_massages()
a.message_user(b, "Пока")
b.get_massages()