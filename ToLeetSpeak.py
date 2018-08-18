def to_leet_speak(str):
    newstr = ""
    for letter in str:
        if letter == "A":
            newstr.append("@")
        elif letter == "B":
            newstr.append("8")
        elif letter == "C":
            newstr.append("(")
        elif letter == "E":
            newstr.append("3")
        elif letter == "G":
            newstr.append("6")
        elif letter == "H":
            newstr.append("#")
        elif letter == "I":
            newstr.append("!")
        elif letter == "L":
            newstr.append("1")
        elif letter == "O":
            newstr.append("0")
        elif letter == "S":
            newstr.append("$")
        elif letter == "T":
            newstr.append("7")
        elif letter == "Z":
            newstr.append("2")
        else:
            newstr.append(letter)
    return str
