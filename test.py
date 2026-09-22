def SelectionSortDesc(l: list) -> list:
    n = len(l)

    for i in range(n):
        # Assume the current position holds the largest remaining value
        max_idx = i

        # Scan the unsorted remainder for something bigger
        for j in range(i + 1, n):
            if l[j] > l[max_idx]:
                max_idx = j

        # Place the largest found into position i
        l[i], l[max_idx] = l[max_idx], l[i]

    return l


array = list(map(int, input().split()))
SelectionSortDesc(array)
print(array)