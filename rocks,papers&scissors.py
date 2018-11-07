from random import randint
while True:
    player = input('Enter the players choice rock(r),paper(p),scissor(s) and for exit(E):')
    print(player,'vs',end=' ')
    if player == 'E':
        break
    choose = randint(1,3)

    if choose == 1:
        computer='r'
    elif choose==2:
        computer='p'
    else:
        computer='s'
    print(computer)

    if player=='r'and computer=='p':
        print('computer win`s Game ')
    if player=='r'and computer=='s':
        print('players win`s Game ')
    if player=='p'and computer=='s':
        print('computer win`s Game ')
    if player==computer:
        print('DRAWN!!!!')

