from abc import ABC, abstractmethod


class Sounds(ABC):
    def objectName(self):
        print(self.name)

    def voiceObject(self):
        print(self.name + " говорит: "+ self.voice)


class Crow(Sounds):
    def __init__(self,name, voice):
        self.name = name
        self.voice = voice


class Duck(Sounds):
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

a = Crow("Белобока", "Кааар")
b = Duck("Дональд", "Кря")
a.voiceObject()
b.voiceObject()
a.objectName()
b.objectName()
