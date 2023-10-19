from math import gcd
class Ratio:
    def __init__(self, a=1, b=1):
        if b == 0:
            raise ZeroDivisionError("Division By Zero!")
        elif type(a) != int or type(b) != int:
            raise ValueError("Enter Integers Only")
        else:
            self.a = a
            self.b = b
            self.decimal = self.a/self.b
            self.mixednum = 0

    def __str__(self):
        return str(self.a) + "/" + str(self.b)

    def lowest_terms(self):
        temp = gcd(self.a, self.b)
        self.a //= temp
        self.b //= temp

    def multiply(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            self.a = self.a * a
            self.decimal = self.a / self.b
        else:
            self.a = self.a * a.a
            self.b = self.b * a.b
            self.decimal = self.a / self.b

    def divide(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            self.b = self.b * a
            self.decimal = self.a / self.b
        else:
            self.a = self.a * a.b
            self.b = self.b * a.a
            self.decimal = self.a / self.b

    def add(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            self.a = self.a + (self.b * a)
            self.decimal = self.a / self.b
        else:
            temp = self.b
            self.b = self.b * a.b
            self.a = (self.a * a.b) + (a.a * temp)
            self.lowest_terms()
            self.decimal = self.a / self.b

    def subtract(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            self.a = self.a - (self.b * a)
            self.decimal = self.a / self.b
        else:
            temp = self.b
            self.b = self.b * a.b
            self.a = (self.a * a.b) - (a.a * temp)
            self.lowest_terms()
            self.decimal = self.a / self.b

    def inverse(self):
        temp = self.a
        self.a = self.b
        self.b = temp
        self.decimal = self.a / self.b

    def convert(self):
        return (self.a / self.b)

    def power(self, a):
        if type(a) != Ratio and type(a) != int:
            raise TypeError("Please Enter Required Value")
        elif type(a) == int:
            self.a = self.a**a
            self.b = self.b**a
            self.decimal = self.a / self.b
        else:
            self.a = (self.a**a.a)**(1/a.b)
            self.b = (self.b ** a.a) ** (1 / a.b)
            temp = int(self.a)
            temp2 = int(self.b)
            if self.a == temp and self.b == temp2:
                self.a = int(self.a)
                self.b = int(self.b)
            else:
                self.decimal = self.a / self.b
                self.a = None
                self.b = None

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
    print(obj)


if __name__ == '__main__':
    main()