import sys
import pprint
sys.stdin = open('input_data/1216.txt')

#T = int(input())



# def pal(arr):
#     return arr == arr[::-1], len(arr)


# for t in range(1, 1+10):
#     _ = int(input())
#     N = 100
#     arr = [list(input()) for _ in range(N)]
#     counts = []
#     for i in range(N):
#         for k in range(N):
#             j = 0
#             x_arrs = []
#             while k+j < 100 :
#                 x_arrs.append(arr[i][k+j])
#                 a, b = pal(x_arrs)
#
#                 if a:
#                     counts.append(b)
#                 j += 1
#
#     for k in range(N):
#         for i in range(N):
#             j = 0
#             arrs = []
#             while i+j < 100:
#                 arrs.append(arr[i+j][k])
#                 a, b = pal(arrs)
#
#                 if a:
#                     counts.append(b)
#                 j += 1
#
#     print('#{} {}'.format(t, max(counts)))

def pal(arr):
    return arr == arr[::-1]
# for t in range(1, 1+10):
#     _ = int(input())
#     N = 100
#     arr = [list(input()) for _ in range(N)]
#     counts = []
#     for i in range(N):
#         for k in range(N):
#             j = 0
#             x_arrs = []
#             y_arrs = []
#             while k+j < 100 :
#                 x_arrs.append(arr[i][k + j])
#                 y_arrs.append(arr[k + j][i])
#                 if pal(x_arrs):
#                     counts.append(len(x_arrs))
#                 if pal(y_arrs):
#                     counts.append(len(y_arrs))
#                 j += 1
#     print('#{} {}'.format(t, max(counts)))

def pal(arr):
    return arr == arr[::-1]
for t in range(1, 1+10):
    _ = int(input())
    N = 100
    arr = [input() for _ in range(N)]
    count = 1
    for i in range(N):
        for k in range(N):
            j = 0
            x = ''
            y = ''
            if N-k > count:
                while k+j < 100 :
                    x += arr[i][k + j]
                    y += arr[k + j][i]
                    if pal(x):
                        if len(x) > count:
                            count = len(x)
                    if pal(y):
                        if len(y) > count:
                            count = len(y)
                    j += 1
    print('#{} {}'.format(t, count))






