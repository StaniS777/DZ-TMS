# Задача 1
class Soda:

    def __init__(self, name):
        self.name = name

    def exam(self):
        if self.name == "":
            return print("У вас обычная газировка")
        else:
            return print(f"Ваша газировка имеет {self.name} вкус")


test = Soda("лимонный")
test.exam()
