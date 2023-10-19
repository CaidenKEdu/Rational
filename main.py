class Ratio:
    def __init__(self, a=1, b=1):
        if b == 0:
            raise ZeroDivisionError("Division By Zero!")
        else:
            self.a = a
            self.b = b
            self.decimal = self.a/self.b
            self.mixednum = 0
    def lowest_terms(self):
        for i in range(2, 100000):
            if self.a % i == 0 and self.b % i == 0:
                self.a = int(self.a / i)
                self.b = int(self.b / i)
                break
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
    print(obj.a)
    print(obj.b)
    print("Lowest Terms")
    obj.lowest_terms()
    print(obj.a)
    print(obj.b)
    print("Multiply by a Ratio")
    obj2 = Ratio(4,15)
    obj.multiply(obj2)
    print(obj.a)
    print(obj.b)
    print("Multiply by an Int")
    obj.multiply(5)
    print(obj.a)
    print(obj.b)
    print("Divide By Ratio")
    obj.divide(obj2)
    print(obj.a)
    print(obj.b)
    print("Lowest Terms")
    obj.lowest_terms()
    print(obj.a)
    print(obj.b)
    print("Divide By Int")
    obj.divide(5)
    print(obj.a)
    print(obj.b)
    print("Lowest Terms")
    obj.lowest_terms()
    print(obj.a)
    print(obj.b)
    print("Add A Ratio")
    obj3 = Ratio(1,2)
    obj.add(obj3)
    print(obj.a)
    print(obj.b)
    print("Add An Int")
    obj.add(5)
    print(obj.a)
    print(obj.b)
    print("Subtract A Ratio")
    obj.subtract(obj3)
    print(obj.a)
    print(obj.b)
    print("Subtract An Int")
    obj.subtract(5)
    print(obj.a)
    print(obj.b)
    print("Lowest Terms")
    obj.lowest_terms()
    print(obj.a)
    print(obj.b)
    print("Inverse")
    obj.inverse()
    print(obj.a)
    print(obj.b)
    print("Inverse")
    obj.inverse()
    print(obj.a)
    print(obj.b)
    print("Decimal Convertion")
    print(obj.convert())
    print("Power Of Int")
    obj.power(3)
    print(obj.a)
    print(obj.b)
    print("Add An Int")
    obj.add(5)
    print(obj.a)
    print(obj.b)
    print("Lowest Terms")
    obj.lowest_terms()
    print(obj.a)
    print(obj.b)
    print("Power of Ratio, Rational")
    obj4 = Ratio(36, 49)
    obj4.power(obj3)
    print(obj4.a)
    print(obj4.b)
    print("Power of Ratio, Non Rational")
    obj.power(obj2)
    print(obj.a)
    print(obj.b)
    print(obj.decimal)
    print("Percentage")
    print(obj4.percent())
    print("Inverse")
    obj4.inverse()
    print(obj4.a)
    print(obj4.b)
    print("Mixed Fractions")
    obj4.mixed()
    print(obj4.mixednum)
    print(obj4.a)
    print(obj4.b)

main()