def sort_list(AList):
    n = len(AList)
    i = 0
    k = n-i-1
    while i < n:
        j = 0
        while j < k:
            if AList[i] < AList[j]:
                temp = AList[j]
                AList[j] = AList[i]
                AList[i] = temp
            j += 1
        i += 1
    return AList