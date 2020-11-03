import sys

sys.stdin = open("input_data/4008_숫자만들기.txt")


# T = int(input())
#
# t = {
#     '0':'+',
#     '1':'-',
#     '2':'*',
#     '3':'/'
# }
#
#
# def game(k, n, result, check):
#     global mins, maxs
#     if k == n - 1:
#         if maxs <= result:
#             maxs = result
#         if mins >= result:
#             mins = result
#         return
#     else:
#         for i in range(len(arr)):
#             if visit[i] == 0:
#                 check += str(arr[i])
#                 if visits.get((check, k), 1):
#                     visits[(check, k)] = 0
#                     visit[i] = 1
#                     if arr[i] == '+':
#                         temp = result + numbers[k + 1]
#                     if arr[i] == '-':
#                         temp = result - numbers[k + 1]
#                     if arr[i] == '*':
#                         temp = result * numbers[k + 1]
#                     if arr[i] == '/':
#                         temp = int(result / numbers[k + 1])
#                     game(k + 1, n, temp, check)
#                     check = check[0:-1]
#                     visit[i] = 0
#
#
# for test_case in range(1, T+1):
#     N = int(input())
#     arrs = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))
#
#     arr = []
#     for i in range(len(arrs)):
#         arr += (t[str(i)] * arrs[i])
#     visit = [0] * len(arr)
#
#     mins = 1231231237298
#     maxs = 0
#     visits = {}
#     game(0, N, numbers[0], '')
#     print('#{} {}'.format(test_case, maxs-mins))




T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arrs = list(map(int, input().split()))
    numbers = list(map(int, input().split()))


    def game(k, n, result):
        global maxs
        global mins
        if k == n - 1:
            if maxs <= result:
                maxs = result
            if mins >= result:
                mins = result
            return
        else:
            for i in range(4):
                if arrs[i] > 0:
                    arrs[i] -= 1
                    if i == 0:
                        temp = result + numbers[k + 1]
                    elif i == 1:
                        temp = result - numbers[k + 1]
                    elif i == 2:
                        temp = result * numbers[k + 1]
                    elif i == 3:
                        temp = int(result / numbers[k + 1])
                    game(k + 1, n, temp)
                    arrs[i] += 1


    maxs = -3213213120
    mins = 1238124

    game(0, N, numbers[0])
    print('#{} {}'.format(test_case, maxs - mins))