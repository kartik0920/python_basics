"""
syntax=
class class_name:
    def __init__(pararmetrs):  this is construction function


here self is like this-> in c++
"""

import os

from dotenv import load_dotenv


class Animal:
    def __init__(self):
        pass

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed=None):
        self.name = name
        self.breed = breed


load_dotenv()
some_key = os.environ.get("some_cred")
print(some_key)
d1 = Dog(name="Kiitu")
d1.eat()
