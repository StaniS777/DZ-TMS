# Задача 5
class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        else:
            if (len(self) % len(s)) == 0:
                n = len(self) // len(s)
                self_1 = n * s
                if self == self_1:
                    return True
                else:
                    return False
            else:
                return False

    def is_palindrome(self):
        if self.lower() == self[::-1].lower():
            return True
        else:
            return False


test = SuperStr('qwqwqwqwqw')
print("is_palindrome ", test.is_palindrome())
print("is_repeatancetest ", test.is_repeatance("qw"))
