a = int(input('enter the number:'))
for i in range(0,a):
    for j in range(0,a-i-1):
        print(end=' ')
    for j in range(0,i+1):
        print('* ',end='')
    print()
