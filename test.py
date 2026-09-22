
def bubble_sort(l):
    n = len(l)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

        if not swapped:
            break


array = list(map(int, input().split()))
bubble_sort(array)
print(array)