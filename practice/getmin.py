arr =[69, 10, 30, 2, 16, 8, 31, 22, 30]
N =len(arr)

# def getMin(s, e):
#     global mins
#     if s == e:
#         print(mins)
#         return mins
#     else:
#         if not mins:
#             mins = arr[e]
#         elif mins >= arr[e]:
#             mins = arr[e]
#         getMin(s, e-1)

mins = 0


def getMin(s, e):

    if s == e:
        return s
    else:

        ret = getMin(s, e-1)
        return ret if arr[ret] < arr[e] else e

print(getMin(0, N -1))


def selectionSort(s, e):
    if s == e:
        return

    idx = getMin(s,e)
    arr[s], arr[idx] = arr[idx], arr[s]
    selectionSort(s+1, e)

selectionSort(0, N-1)
print(arr)
