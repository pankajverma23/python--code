print("Note:if you Want to exit then enter [E] ")
while True:
    No=input('Enter the no you between "1" to "6":')
    if No == 'E':
        break
    try:
        N = float(No)
    except ValueError:
        print('I said!! Enter the the between the 1 to 6')
    else:
        if N == 1:
            print('The output of dice 1')
        elif N == 2:
            print('The output of dice 2')
        elif N == 3:
            print('The output of dice 3')
        elif N == 4:
            print('The output of dice 4')
        elif N == 5:
            print('The output of dice 5')
        elif N == 6:
            print('The output of dice 6')
        else:
            print(N,'this Number is not exist on the dice')
