print("=======This Project For Fibonacci Sequence======")
N = input('Enter the no:')
try:
    num = int(N)
except ValueError:
    print("i said Enter positive Integer no!!!!!!!!!!")

n1 = 0
n2 = 1
count =0
print('fibonacci sequence of',num,':')
while count <=num:
    print(n1)
    n3 =n1+n2
    n1=n2
    n2=n3
    count+=1
