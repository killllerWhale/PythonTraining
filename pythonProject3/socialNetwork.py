from abc import ABC, abstractmethod

class Social_Network(ABC):

    def message_user(self, user, message):
        user.messages.append(message)

    def message_wall(self, message):
        self.messages.append(message)

    @abstractmethod
    def dop_info(self):
        pass

    def printinfo_user(self):
        print("Имя пользователя: " + self.name+" ")
        self.dop_info()

class user(Social_Network):

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_birth = date_of_birth
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
        self.user_subscriptions = []

    def dop_info(self):
        print("Описание: " + str(self.description))
