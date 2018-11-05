
class student:
    def __init__(self,name):
        self.name = name
        self.marks=[]
        print('welcom {} to the college'.format(name))

    def addmarks(self,marks):
        self.marks.append(marks)

    def avg(self):
        p=sum(self.marks)
        print(p)
        a=len(self.marks)
        print(a)
        return p/a


s=student(input('Enter the Name:'))
print('entered name is:',s.name)
s.addmarks(input("enter the 1 marks:"))
s.addmarks(input("enter the 2 marks:"))
s.addmarks(input("enter the 3 marks:"))
s.addmarks(input("enter the 4 marks:"))
print('entered mark is:',s.marks)
print('entered mark is:',s.avg())




