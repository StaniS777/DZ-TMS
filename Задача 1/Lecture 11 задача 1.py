# Задача 1
class Soda:

    def __init__(self, name):
        self.name = name

    def exam(self):
        if self.name == "":
            print("У вас обычная газировка")
        else:
            print(f"Ваша газировка имеет {self.name} вкус")


taste = input("Введите вкус: ")
name = Soda(taste)
name.exam()
