from math import gcd
class Ratio:
    def __init__(self, a=1, b=1):
        if b == 0:
            raise ZeroDivisionError("Division By Zero!")
        elif a != None or b != None:
            self.a = a
            self.b = b
            self.decimal = self.a / self.b
            self.mixednum = 0
        elif type(a) != int or type(b) != int:
            raise ValueError("Enter Integers Only")
        else:
            self.a = a
            self.b = b
            self.decimal = self.a/self.b
            self.mixednum = 0
            self.lowest_terms()

    def __str__(self):
        if self.a == None or self.b == None:
            return str(self.decimal)
        else:
            if self.b == 1:
                return str(self.a)
            return str(self.a) + "/" + str(self.b)

    def __add__(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            temp_a = self.a + (self.b * a)
            obj = Ratio(temp_a, self.b)
        else:
            temp = self.b
            temp_b = self.b * a.b
            temp_a = (self.a * a.b) + (a.a * temp)
            obj = Ratio(temp_a, temp_b)
        return obj

    def __sub__(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            temp_a = self.a - (self.b * a)
            obj = Ratio(temp_a, self.b)
        else:
            temp = self.b
            temp_b = self.b * a.b
            temp_a = (self.a * a.b) - (a.a * temp)
            obj = Ratio(temp_a, temp_b)
        return obj

    def __truediv__(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            temp_b = self.b * a
            obj = Ratio(self.a, temp_b)
        else:
            temp_a = self.a * a.b
            temp_b = self.b * a.a
            obj = Ratio(temp_a, temp_b)
        return obj

    def __mul__(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            temp_a = self.a * a
            obj = Ratio(temp_a, self.b)
        else:
            temp_a = self.a * a.a
            temp_b = self.b * a.b
            obj = Ratio(temp_a, temp_b)
        return obj

    def __pow__(self, a, modulo = None):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            temp_a = self.a**a
            temp_b = self.b**a
            obj = Ratio(temp_a, temp_b)
        else:
            temp_a = (self.a**a.a)**(1/a.b)
            temp_b = (self.b ** a.a) ** (1 / a.b)
            temp = int(self.a)
            temp2 = int(self.b)
            if temp_a == temp and temp_b == temp2:
                temp_a = int(self.a)
                temp_b = int(self.b)
                obj = Ratio(temp_a, temp_b)
            else:
                obj = Ratio(temp_a, temp_b)
                obj.a = None
                obj.b = None
        return obj

    def lowest_terms(self):
        temp = gcd(self.a, self.b)
        self.a //= temp
        self.b //= temp

    def __invert__(self):
        temp = self.a
        self.a = self.b
        self.b = temp
        self.decimal = self.a / self.b

    def __neg__(self):
        self.a = -self.a

    def convert(self):
        return (self.a / self.b)

    def percent(self):
            return((self.a/self.b)*100)

    def mixed(self):
        if self.b < self.a:
            for i in range(self.a):
                if i % self.b == 0:
                    self.mixednum = int(i / self.b)
                    self.a = self.a - int((i / self.b)*self.b)

def main():
    print("Init")
    obj = Ratio(2, 6)
    obj2 = Ratio(9, 20)
    print(obj)



if __name__ == '__main__':
    main()