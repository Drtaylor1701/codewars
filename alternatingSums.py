def alternatingSums(a):
    index = 0
    team1 = 0
    team2 = 0
    for element in a:
        if index % 2 == 0:
            team1 = team1 + element
        else:
            team2 = team2 + element
        index += 1
    return [team1, team2]
