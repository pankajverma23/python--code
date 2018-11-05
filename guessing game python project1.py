print('input [E] for exit')
while True:
    inp = input('enter a number:')
    if inp == 'E':
        break
    try:
        number = float(inp)
    except:
        print('I said! input should be a Number ')

    else:
        test = number%2
        if test == 0:
            print(int(number),'Number is even')
        elif test == 1:
            print(int(number),'number is odd')
        else:
            print(number,'is very strange')



