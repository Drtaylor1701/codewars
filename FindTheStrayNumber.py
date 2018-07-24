def stray(arr):
    notzero = 0
    for number in arr:
        if number != arr[0]:
            print(number)
            return(number)
    notzero = 1
    if notzero == 1:
        print(arr[0])
        return(arr[0])
