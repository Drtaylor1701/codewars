def maxSequence(arr):
    sum = 0
    lessThanZero = 0
    total = 0
    greaterThanZero = 0
    if arr == []:
        output = 0
        return output
    else:
        for i in arr:
            if i < 0:
                lessThanZero += 1
                if lessThanZero == len(arr):
                    output = 0
                    return output
            elif i > 0:
                greaterThanZero += 1
                if greaterThanZero == len(arr):
                    total = total + i
                    output = total
                    print(output)
                    return output
            else:
                index = 1
                totals = []
                for i in arr:
                    total = i + arr[index]
                    totals.append(total)
                    if index > len(arr):
                        index += 1

arr = []
maxSequence(arr)
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSequence(arr)
