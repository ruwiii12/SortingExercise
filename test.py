
def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop to access each array element
    for i in range(n):
        swapped = False
        
        # Inner loop for adjacent comparisons
        # (n - i - 1) stops us from checking already sorted elements at the end
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements using Python's clean tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break


array = input()
bubble_sort(array)