# Задача 1
class Soda:

    def __init__(self, name=""):
        self.name = name

    def exam(self):
        if self.name == "":
            return "У вас обычная газировка"
        else:
            return f"Ваша газировка имеет {self.name} вкус"


test = Soda()
print(test.exam())
