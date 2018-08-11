def solution(string1, string2):
    string2Length = len(string2)
    print(string2Length)
    string2Length = -string2Length
    print(string2Length)
    print(string1[string2Length:])
    string1Slice = string1[string2Length:]
    print(string1Slice)
    if string1Slice == string2:
        return True
    else:
        return False

solution('abcde', 'cde')
