from typing import AsyncGenerator


class Student:


    def__init__(self, name, age):
        self.name = name
        self.age = age

    John = Student("John, "21")
    Jane = Student("Jane", "22")

print(getattr(John,"age"))
