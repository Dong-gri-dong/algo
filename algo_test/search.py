def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start + (end-start) // 2

        if key == a[middle]:
            return True

        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return False

a = [1, 3, 5,12, 31, 32, 40]

print(binarySearch(a, 32))

def binaryserach(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        middle = start + (start + end)//2

        if a[middle] == key:
            return True
        elif key < a[middle]:
            end = middle-1
        else:
            key > a[middle]
            start = middle+1

    return False