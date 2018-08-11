def addBorder(picture):
    index = 0
    topBottom = len(picture) / 2
    topBottom = int(topBottom)
    top = "**" * topBottom + "**"
    newArray = [top]
    for element in picture:
        newArray.append("*" + element + "*")

    newArray.append(top)
    return newArray
