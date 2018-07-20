def number(bus_stops):
    people = 0
    # Good Luck!
    for array in bus_stops:
        print(array)
        index = 0
        for number in array:
            print(number)
            if index == 0:
                people = people + number
            else:
                people = people - number
            print(people)
    print(people)

bus_stops = [[10,0],[3,5],[5,8]]
number(bus_stops)
