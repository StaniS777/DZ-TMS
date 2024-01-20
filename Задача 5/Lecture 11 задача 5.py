# Задача 5
class SuperStr(str):
    def __init__(self, s):
        self.s = s

    def is_repeatance(self, s_str):
        value = len(self.s) % len(s_str)
        if value == 0:
            print("True - строка получена целым количеством повторов строки s")
        else:
            print("False - строка НЕ получена целым количеством повторов строки s")

    def is_palindrome(self):
        if self.s.lower() == self.s[::-1].lower():
            print("Палиндром")
        else:
            print("Не палиндром")


test = SuperStr('qwertytrewq')
test.is_palindrome()
test.is_repeatance("1234")
