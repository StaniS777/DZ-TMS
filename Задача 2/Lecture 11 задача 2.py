# Задача 2
class Math:

    def addition(self, num_1, num_2):
        print(f"{num_1} + {num_2} = {num_1 + num_2}")

    def subtraction(self, num_1, num_2):
        print(f"{num_1} - {num_2} = {num_1 - num_2}")

    def multiplication(self, num_1, num_2):
        print(f"{num_1} * {num_2} = {num_1 * num_2}")

    def division(self, num_1, num_2):
        print(f"{num_1} / {num_2} = {(num_1 / num_2):.2f}")


exam = Math()
exam.addition(1, 2)
exam.subtraction(5, 3)
exam.multiplication(2, 3)
exam.division(6, 3)
