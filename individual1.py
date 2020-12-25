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

class Triangle:
    
    def __init__(self, FirstSide=0, SecondSide=0, ThirdSide=0, FirstAngle=0, SecondAngle=0, ThirdAngle=0):
        self.FirstSide = FirstSide
        self.SecondSide = SecondSide
        self.ThirdSide = ThirdSide
        self.FirstAngle = FirstAngle
        self.SecondAngle = SecondAngle
        self.ThirdAngle = ThirdAngle

    def read(self, prompt=None):
        if prompt:
            print(prompt)
        self.FirstSide = int(input("Введите значение первой стороны: "))
        self.SecondSide = int(input("Введите значение второй стороны: "))
        self.ThirdSide = int(input("Введите значение третьей стороны: "))
        self.FirstAngle = int(input("Введите значение первого угла: "))
        self.SecondAngle = int(input("Введите значение второго угла "))
        self.ThirdAngle = int(input("Введите значение третьего угла: "))
        
    def display(self):
        print(self.FirstSide, self.SecondSide, self.ThirdSide)
        print(self.FirstAngle, self.SecondAngle, self.ThirdAngle)
    
    def get_FirstSide(self):
        return self.FirstSide

    def get_SecondSide(self):
        return self.SecondSide
    
    def get_ThirdSide(self):
        return self.ThirdSide

    def get_FirstAngle(self):
        return self.FirstAngle

    def get_SecondAngle(self):
        return self.SecondAngle
    
    def get_ThirdAngle(self):
        return self.ThirdAngle

    def set_FirstSide(self, fs):
        self.FirstSide = fs

    def set_SecondSide(self, ss):
        self.SecondSide = ss

    def set_ThirdSide(self, ts):
        self.ThirdSide = ts

    def set_FirstAngle(self, fa):
        self.FirstAngle = fa

    def set_SecondAngle(self, sa):
        self.SecondAngle = sa

    def set_ThirdAngle(self, ta):
        self.ThirdAngle = ta

    def area(self):
        p = (self.FirstSide + self.SecondSide + self.ThirdSide)/2  # полупериметр треугольника
        return (p*(p - self.FirstSide)*(p - self.SecondSide)*(p - self.ThirdSide))**(1/2)  # формула Герона
    
    def perimetr(self):
        return self.FirstSide + self.SecondSide + self.ThirdSide

    def firstheight(self):
        p = (self.FirstSide + self.SecondSide + self.ThirdSide)/2  # полупериметр треугольника
        return round(2*(p*(p - self.FirstSide)*(p - self.SecondSide)*(p - self.ThirdSide))**(1/2)/self.FirstSide, 2)

    def secondheight(self):
        p = (self.FirstSide + self.SecondSide + self.ThirdSide)/2  # полупериметр треугольника
        return round(2*(p*(p - self.FirstSide)*(p - self.SecondSide)*(p - self.ThirdSide))**(1/2)/self.SecondSide, 2)

    def thirdheight(self):
        p = (self.FirstSide + self.SecondSide + self.ThirdSide)/2  # полупериметр треугольника
        return round(2*(p*(p - self.FirstSide)*(p - self.SecondSide)*(p - self.ThirdSide))**(1/2)/self.ThirdSide, 2)

    def definition(self):
        if self.FirstAngle == 90 or self.SecondAngle == 90 or self.ThirdAngle == 90:
            print("Треугольник прямоугольный")
        
        if self.FirstSide == self.SecondSide == self.ThirdSide:
            print("Треугольник равносторонний")

        elif self.FirstSide == self.SecondSide or self.FirstSide == self.ThirdSide or self.SecondSide == self.ThirdSide:
            print("Треугольник равнобедренный")
        

if __name__ == "__main__":
    my_triangle = Triangle(3, 4, 5, 90, 30, 60)
    print(my_triangle.get_FirstSide())
    # my_triangle.set_FirstSide(5)
    print(my_triangle.get_FirstSide())
    print("AREA ", my_triangle.area())
    print("PERIMETR ", my_triangle.perimetr())
    # my_tri = Triangle()
    # my_tri.read("Введите значения ниже")
    # my_tri.display()
    print(my_triangle.firstheight())
    my_triangle.definition()
    print("New-triangle")
    new_triangle = Triangle(6, 6, 6, 60, 60, 60)
    new_triangle.definition()
    print(new_triangle.firstheight())
    print(new_triangle.secondheight())
    print(new_triangle.thirdheight())
