from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def ret_coordinates(self):
        return [self.x,self.y,self.z]

class Object(Base):
    def allNone(self):
        self.x = None
        self.y = None
        self.z = None

class Subject(Base):
    def new_coordinates (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Nomethods(Base):
    pass