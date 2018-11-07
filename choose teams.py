from random import choice
players=['pankaj','radhe','ayush','ritesh','rana','shubham','aman','vikash']
teamA=[]
teamB=[]
while len(players)>0:

    playersA=choice(players)
    teamA.append(playersA)
    players.remove(playersA)


    playersB = choice(players)
    teamB.append(playersB)
    players.remove(playersB)



print('Team A players:',teamA)
print('Team B players:',teamB)
