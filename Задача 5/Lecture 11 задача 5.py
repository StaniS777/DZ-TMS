# Задача 5
class SuperStr(str):
    def __init__(self, s):
        self.s = s
        super().__init__()

    def is_repeatance(self, s_str):
        value = len(self.s) % len(s_str)
        if value == 0:
            return True
        else:
            return False

    def is_palindrome(self):
        if self.s.lower() == self.s[::-1].lower():
            return True
        else:
            return False


test = SuperStr('qwertytrewq')
print(test.is_palindrome())
print(test.is_repeatance("1234"))
