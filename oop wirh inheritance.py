class calculator(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x + self.y
    def mult(self):
        return self.x * self.y

class sc(calculator):
    def power(self):
        return pow(self.x,self.y)


c=calculator(23,45)
print('sum of x & y is :',c.add())
print('multiplication of x & y is :',c.mult())

s =sc(10,20)
print('power of x & y is :',s.power())