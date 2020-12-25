# 16. Создать базовый класс Pair(пара целых чисел) 
# с операциями проверки на равенство и
# перемножения полей.
# Реализовать операцию вычитания пар по формуле
# (a, b)-(c, d) = (a-b, c-d).

# Создать производный класс Rational
# определить новые операции сложения
# (a, b)+(c, d) = (ad+bc, bd) 
# и деления(a, b)/(c, d) = (ad, bc),
# переопределить операцию вычитания
# (a, b)-(c, d) = (ad-bc, bd).

class Pair:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def isequal(self):
        return self.a == self.b

    def multiply(self):
        return self.a * self.b

    def sub(self, other):
        print("({0}, {1})".format(self.a - self.b, other.a - other.b))
        

class Rational(Pair):
    def add(self, other):
        print("({0}, {1})".format(self.a * other.b + self.b * other.a, self.b * other.b))

    def div(self, other):
        print("({0}, {1})".format(self.a * other.b, self.b * other.a))

    def sub(self, other):
        print("({0}, {1})".format(self.a * other.b - self.b * other.a, self.b * other.b))


if __name__ == "__main__":
    my_pair = Pair(2, 1)
    print(my_pair.isequal())
    print(my_pair.multiply())
    new_pair = Pair(3, 2)
    print(new_pair.isequal())
    print(new_pair.multiply())
    my_pair.sub(new_pair)

    my_rat = Rational(2, 1)
    new_rat = Rational(3, 2)
    my_rat.add(new_rat)
    my_rat.div(new_rat)
    my_rat.sub(new_rat)

