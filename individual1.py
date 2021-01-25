#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triangle для представления треугольника.
# Поля данных должны включать
# углы и стороны.
# Требуется реализовать операции:
# получения и изменения полей данных,
# вычисления площади,
# вычисления периметра,
# вычисления высот,
# а также определения вида треугольника
# (равносторонний, равнобедренный или прямоугольный).

from math import acos, pi


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class Triangle:

    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c
        self.check()

    def check(self):
        try:
            if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
                raise MyError("Ошибка - треугольник не существует")
        except MyError as mr:
            print(mr)

    def alpha(self):
        return round(acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)) * 180 / pi, 1)

    def beta(self):
        return round(acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)) * 180 / pi, 1)

    def gamma(self):
        return round(acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.c * self.b)) * 180 / pi, 1)

    def read(self, prompt=None):
        if prompt:
            print(prompt)
        self.a = int(input("Введите значение первой стороны: "))
        self.b = int(input("Введите значение второй стороны: "))
        self.c = int(input("Введите значение третьей стороны: "))
        self.check()

    def display(self):
        print(self.a, self.b, self.c)
        try:
            print(self.alpha(), self.beta(), self.gamma())
        except ValueError:
            print("Ошибка - вычисление невозможно")

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_alpha(self):
        return self.alpha

    def get_beta(self):
        return self.beta

    def get_gamma(self):
        return self.gamma

    def set_a(self, fs):
        self.a = fs

    def set_b(self, ss):
        self.b = ss

    def set_c(self, ts):
        self.c = ts

    def set_alpha(self, fa):
        self.alpha = fa

    def set_beta(self, sa):
        self.beta = sa

    def set_gamma(self, ta):
        self.gamma = ta

    def area(self):
        # полупериметр треугольника
        p = (self.a + self.b + self.c) / 2
        # формула Герона
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)

    def perimetr(self):
        return self.a + self.b + self.c

    def firstheight(self):
        return round(2 * self.area() / self.a, 2)

    def secondheight(self):
        return round(2 * self.area() / self.b, 2)

    def thirdheight(self):
        return round(2 * self.area() / self.c, 2)

    def definition(self):
        if self.alpha == 90 or self.beta == 90 or self.gamma == 90:
            print("Треугольник прямоугольный")

        if self.a == self.b == self.c:
            print("Треугольник равносторонний")

        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Треугольник равнобедренный")


if __name__ == "__main__":
    my_triangle = Triangle(3, 4, 5)
    print(my_triangle.get_a())
    # my_triangle.set_a(5)
    print(my_triangle.get_a())
    print("AREA ", my_triangle.area())
    print("PERIMETR ", my_triangle.perimetr())
    print()
    my_tri = Triangle()
    my_tri.read("Введите значения ниже")
    my_tri.display()
    print()
    print(my_triangle.firstheight())
    my_triangle.definition()
    print("New-triangle")
    new_triangle = Triangle(6, 5, 4)
    new_triangle.definition()
    print(new_triangle.firstheight())
    print(new_triangle.secondheight())
    print(new_triangle.thirdheight())
    new_triangle.display()
