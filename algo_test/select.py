a = [64, 25, 10, 22, 11]


def select(a, k):
    for i in range(k):
        min_index = i
        for j in range(i, k):
            if a[min_index] >= a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a[k]

print(select(a, 3))