arrs = [1, 2]
temp = []
def comb(n, r):
    if r == 0:
        print(temp)
    elif n < r:
        return
    else:
        temp.append(arrs[n-1])
        comb(n-1, r-1)
        comb(n-1, r)




# temp = []
# def perm(arr, depth, n, k):
#     # depth가 0부터 시작하여 k라면 k개를 모두 뽑은 것이므로 print하고 return
#     if (depth == k):
#         print(arr)
#         return
#     for idx in range(depth, n):
#         # 각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고,
#         # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고,
#         # 원상복구 하여 다시 경우의 수를 찾는다
#         arr[idx], arr[depth] = arr[depth], arr[idx]
#         perm(arr, depth+1, n, k)
#         arr[idx], arr[depth] = arr[depth], arr[idx]
#
# perm(arrs, 0, len(arrs), len(arrs)-1)


def perm(arr, k, n):
    if (k == n-1):
        print(arr)
        return
    for idx in range(k, n):
        arr[idx], arr[k] = arr[k], arr[idx]
        perm(arr, k+1, n)
        arr[idx], arr[k] = arr[k], arr[idx]

perm(arrs, 0, len(arrs))


arr = [10, 20, 30, 40]


def perm(k, n):

    if k == n-1:
        print(arr)
        return

    for i in range(k, n):
        arr[i], arr[k] = arr[k], arr[i]
        perm(k + 1, n)
        arr[i], arr[k] = arr[k], arr[i]



perm(0, len(arr))
