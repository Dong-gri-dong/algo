import sys
import pprint
sys.stdin = open('input_data/4615.txt')



# T = int(input())


# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#
#     arr = [[0]*N for _ in range(N)]
#
#     center = N // 2
#     c= [2, 1, 1, 2]
#     count = 0
#     for i in range(center-1, center+1):
#         for k in range(center-1, center+1):
#             arr[i][k] = c[count]
#             count += 1
#
#
#
#     for _ in range(M):
#         k, i, color = map(int, input().split())
#
#         i -= 1
#         k -= 1
#
#         arr[i][k] = color
#         change = []
#
#         j = 1
#         change_s = []
#         while k+j < N:
#             if arr[i][k+j] != 0 and arr[i][k+j] != color:
#                 change_s.append([i, k+j])
#                 j += 1
#             elif arr[i][k+j] == 0:
#                 break
#             else:
#                 change.extend(change_s)
#                 break
#
#         j = 1
#         change_s = []
#         while k - j >= 0:
#             if arr[i][k - j] != 0 and arr[i][k - j] != color:
#
#                 change_s.append([i, k - j])
#                 j += 1
#             elif arr[i][k - j] == 0:
#                 break
#             else:
#                 change.extend(change_s)
#                 break
#
#         j = 1
#         change_s = []
#
#         while i+j < N:
#             if arr[i+j][k] != 0 and arr[i+j][k] != color:
#                 change_s.append([i+j, k])
#                 j += 1
#             elif arr[i + j][k] == 0:
#                 break
#
#
#             else:
#                 change.extend(change_s)
#                 break
#
#         j = 1
#         change_s = []
#         while i - j >= 0:
#             if arr[i - j][k] != 0 and arr[i - j][k] != color:
#                 change_s.append([i - j, k])
#
#                 j += 1
#             elif arr[i - j][k] == 0:
#                 break
#
#             else:
#                 change.extend(change_s)
#                 break
#
#         j = 1
#         change_s = []
#         while i+j < N and k+j < N:
#             if arr[i+j][k+j] != 0 and arr[i+j][k+j] != color:
#                 change_s.append([i+j, k+j])
#                 j += 1
#             elif arr[i + j][k + j] == 0:
#                 break
#             else:
#                 change.extend(change_s)
#                 break
#
#         j = 1
#         change_s = []
#         while i-j >= 0 and k-j >= 0:
#             if arr[i-j][k-j] != 0 and arr[i-j][k-j] != color:
#                 change_s.append([i-j, k-j])
#                 j += 1
#             elif arr[i - j][k - j] == 0:
#                 break
#
#             else:
#                 change.extend(change_s)
#                 break
#
#
#
#         j = 1
#         change_s = []
#         while i+j < N and k-j >= 0:
#             if arr[i+j][k-j] != 0 and arr[i+j][k-j] != color:
#                 change_s.append([i+j, k-j])
#                 j += 1
#             elif arr[i + j][k - j] == 0:
#                 break
#
#             else:
#                 change.extend(change_s)
#                 break
#
#         j = 1
#         change_s = []
#         while i-j >= 0 and k+j < N:
#             if arr[i-j][k+j] != 0 and arr[i-j][k+j] != color:
#                 change_s.append([i-j, k+j])
#                 j += 1
#             elif arr[i - j][k + j] == 0:
#                 break
#
#             else:
#                 change.extend(change_s)
#                 break
#
#         for i in range(len(change)):
#             x, y = change[i]
#             arr[x][y] = color
#
#
#     count_w = 0
#     count_b = 0
#     for i in range(N):
#         for k in range(N):
#             if arr[i][k] == 1:
#                 count_b += 1
#             elif arr[i][k] == 2:
#                 count_w += 1
#
#     print('#{} {} {}'.format(test_case, count_b, count_w))


# ????????????

#   ??????, ??????, ??????, ??????, ?????????, ?????????, ?????????, ?????????
T = int(input())

dx = [1,  -1,   0,   0,    1,     1,     -1,   -1]
dy = [0,   0,  -1,   1,    -1,     1,     -1,    1]


for test_case in range(1, T+1):
    N, M = map(int, input().split())
    #N??? ????????? ????????? N x N
    #M??? ????????? ??????

    # 0????????? NxN ?????????

    arr = [[0]*N for _ in range(N)]
    # ???????????? ??? ?????????
    # W : 2  B : 1
    center = N // 2
    c= [2, 1, 1, 2]
    count = 0
    for i in range(center-1, center+1):
        for k in range(center-1, center+1):
            arr[i][k] = c[count]
            count += 1
    # ????????? ?????? ????????? ?????? ?????? ?????? ??????
    # pprint.pprint(arr, width=20)

    #??? ?????? ????????? ??? ??????
    for _ in range(M):

        # i k??? ????????? k i??? ?????? ????????? ???????????? 2, 3??? ???????????? 3-1, 2-1??? ??????
        # ????????? arr?????? ?????? arr[i][k] ????????? ????????? ?????????
        k, i, color = map(int, input().split())

        # ???????????? 0?????? ??????????????? 1????????????.
        i -= 1
        k -= 1

        # ?????? ?????????
        arr[i][k] = color

        # 8????????????????????? range(8)
        change = []

        for j in range(8):
            # 8????????? ???????????? ????????? ?????? ?????????????????? ????????? ??????
            # ??????, ??????, ??????, ??????, ?????????, ?????????, ?????????, ?????????
            ti = i + dx[j]
            tk = k + dy[j]
            # ????????? ???????????? ?????? ???????????? ??????
            change_8 =[]
            while 0 <= ti <N and 0 <= tk < N:
                # ????????? ?????? ??????????????? ????????? W??? B?????? B????????? W??? ??????
                if arr[ti][tk] != 0 and arr[ti][tk] != color:

                    change_8.append([ti, tk])
                    ti += dx[j]
                    tk += dy[j]

                # ????????? ?????? ???????????? 0??? ????????? ????????? ???????????? ????????? ????????? break
                elif arr[ti][tk] == 0:
                    break

                # ????????? ?????? ?????? ?????? ???????????? ????????? ???????????? ????????? ????????? ????????? ?????????
                # break
                else:
                    change.extend(change_8)
                    break

        # ????????? ????????? ?????? ????????????.
        for n in range(len(change)):
            x, y = change[n]
            arr[x][y] = color

    # ??????????????? ????????? ???????????? ????????????.
    count_w = 0
    count_b = 0
    for i in range(N):
        for k in range(N):
            if arr[i][k] == 1:
                count_b += 1
            elif arr[i][k] == 2:
                count_w += 1

    print('#{} {} {}'.format(test_case, count_b, count_w))



