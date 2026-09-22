# Problem 2a
# 
# Input: List l of integers
# Output: Sorted list of integers
#
# Requirements:
# - Implement Bubble Sort (Optimized)
#   (Optimized = No checking of guaranteed sorted elements)
# - Implement 2 versions of the algorithm: one that sorts in ascending order and another in descending order

def BubbleSortOptimizedDesc(l: list) -> list:
    n = len(l)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

        if not swapped:
            break


def BubbleSortOptimizedAsc(l: list) -> list:
    n = len(l)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

        if not swapped:
            break


# Problem 2b
# 
# Input: List l of integers
# Output: Sorted list of integers
# 
# Requirements:
# - Implement Insertion Sort
# - Implement 2 versions of the algorithm: one that sorts in ascending order and another in descending order

def InsertionSortDesc(l: list) -> list:
    for i in range(1, len(l)):
        key, j = l[i], i - 1
        while j >= 0 and l[j] < key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

def InsertionSortAsc(l: list) -> list:
    for i in range(1, len(l)):
        key, j = l[i], i - 1
        while j >= 0 and l[j] > key:  # flipped compared to above 
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

# Problem 2c
# 
# Input: List l of integers
# Output: Sorted list of integers
# 
# Requirements:
# - Implement Selection Sort
# - Implement 2 versions of the algorithm: one that sorts in ascending order and another in descending order

def SelectionSortDesc(l: list) -> list:
    n = len(l)

    for i in range(n):
        max_idx = i

        # Check the unsorted for a bigger value
        for j in range(i + 1, n):
            if l[j] > l[max_idx]:
                max_idx = j

        l[i], l[max_idx] = l[max_idx], l[i]

    return l

def SelectionSortAsc(l: list) -> list:
    pass # Your code here

# Problem 2d
# 
# Input: None; The function asks for three user inputs: String list, String sort, and String direction
#        String list should be only integers separated by a comma and possibly a space (e.g. "1, 2, 3, 4, 5" or "1,2,3,4,5")
#        String sort should only be "bubble", "insertion", or "selection"
#        String direction should either be "asc" or "desc"
# Output: Sorted list of integers (in the desired order)
# 
# Requirements:
# - Use the functions you made in problems 2a - 2c
# - Handle invalid inputs

def Sorter():
    pass # Your code here


'''
use try and except in def Sorter()
'''