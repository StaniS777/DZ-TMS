# Задача 5
class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        else:
            if (len(self) % len(s)) == 0:
                return True
            else:
                return False

    def is_palindrome(self):
        if self.lower() == self[::-1].lower():
            return True
        else:
            return False


test = SuperStr('qwertytrew')
print(test.is_palindrome())
print(test.is_repeatance("12"))
