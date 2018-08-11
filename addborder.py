def addBorder(picture):
    index = 0
    topBottom = "*" * len(picture[0]) + "**"
    newArray = [topBottom]
    for element in picture:
        newArray.append("*" + element + "*")

    newArray.append(topBottom)
    return newArray
