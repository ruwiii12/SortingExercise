def InsertionSortDesc(l: list) -> list:
    for i in range(1, len(l)):
        key, j = l[i], i - 1
        while j >= 0 and l[j] < key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


array = list(map(int, input().split()))
InsertionSortDesc(array)
print(array)