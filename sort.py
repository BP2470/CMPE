def sort_list(AList):
    n = len(AList)
    i = 0
    while i < n:
        j = n - i - 1
        while j < n:
            temp = AList[i]
            AList[i] = AList[j]
            AList[j] = temp
        j = j + 1
    i += 1 
    return AList