import sys

sys.stdin = open("input_data/4880.txt")

T = int(input())



# 1 가위
# 2 바위
# 3 보

# index로 해야할듯 몇번 학생인지 알아야하기 때문에
def match(x, y): # index를 input으로 받아서 사용
    # 1 가위
    # 2 바위
    # 3 보

    # 가위가 이기는 경우(같으면 낮은 번호)
    if arr[x-1] == 1:
        # 보 이거나 같은 경우
        if arr[y-1] == 3 or arr[y-1] == 1:
            return x

    # 바위가 이기는 경우(같으면 낮은 번호)
    elif arr[x-1] == 2:
        # 가위 이거나 같은 경우
        if arr[y-1] == 1 or arr[y-1] == 2:
            return x

    # 보가 이기는 경우(같으면 낮은 번호)
    elif arr[x-1] == 3:
        # 바위 이거나 같은 경우
        if arr[y-1] == 2 or arr[y-1] == 3:
            return x
    return y


for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    N = len(arr)


    # (i+j)//2 까지
    # (i+j)//2+1 부터터

    def dfs(i, j):
        print('ij {} {}'.format(i, j))
        if i == j:
            return i

        else:
            x = dfs(i, (i+j)//2)
            y = dfs(((i + j) // 2) +1, j)

            return match(x, y)






    print('#{} {}'.format(test_case, dfs(1, N)))

    exit()

    # def dfs(arr):
    #
    #     if len(arr) == 1:
    #         return arr[0]
    #
    #     else:
    #         x = dfs(arr[:(len(arr)+1)//2])
    #         y = dfs(arr[(len(arr) + 1) // 2 :])
    #
    #
    #     return match(x,y)






# def match(x, y):
#     # 1 가위
#     # 2 바위
#     # 3 보
#
#     # 가위가 이기는 경우(같으면 낮은 번호)
#     if arr[x-1] == 1:
#         # 보 이거나 같은 경우
#         if arr[y-1] == 3 or arr[y-1] == 1:
#             return x
#
#     # 바위가 이기는 경우(같으면 낮은 번호)
#     elif arr[x-1] == 2:
#         # 가위 이거나 같은 경우
#         if arr[y-1] == 1 or arr[y-1] == 2:
#             return x
#
#     # 보가 이기는 경우(같으면 낮은 번호)
#     elif arr[x-1] == 3:
#         # 바위 이거나 같은 경우
#         if arr[y-1] == 2 or arr[y-1] == 3:
#             return x
#     return y
#
#
# for test_case in range(1, T+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     N = len(arr)
#
#
#     # (i+j)//2 까지
#     # (i+j)//2+1 부터터
#     print(arr)
#     def dfs(i, j):
#         if i == j:
#             print(i)
#             return i
#         x = dfs(i, (i+j)//2)
#         print('x:{}'.format(arr[x-1]))
#
#         y = dfs(((i + j) // 2) +1, j)
#         print('y:{}'.format(arr[y-1]))
#         return match(x, y)
#
#
#
#
#     print('#{} {}'.format(test_case, dfs(1, N)))
