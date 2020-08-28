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


# 방향설정

#   우측, 좌측, 상단, 하단, 우상단, 우하단, 좌상단, 좌하단
T = int(input())

dx = [1,  -1,   0,   0,    1,     1,     -1,   -1]
dy = [0,   0,  -1,   1,    -1,     1,     -1,    1]


for test_case in range(1, T+1):
    N, M = map(int, input().split())
    #N은 오셀로 사이즈 N x N
    #M은 돌놓은 횟수

    # 0으로된 NxN 만들기

    arr = [[0]*N for _ in range(N)]
    # 가운데에 색 채우기
    # W : 2  B : 1
    center = N // 2
    c= [2, 1, 1, 2]
    count = 0
    for i in range(center-1, center+1):
        for k in range(center-1, center+1):
            arr[i][k] = c[count]
            count += 1
    # 이걸로 보면 배열을 보금 쉽게 볼수 있음
    # pprint.pprint(arr, width=20)

    #돌 넣는 좌표와 색 받기
    for _ in range(M):

        # i k로 안받고 k i로 받는 이유는 오셀로의 2, 3은 행렬에서 3-1, 2-1에 해당
        # 그리고 arr할때 내가 arr[i][k] 이것이 편해서 뒤집음
        k, i, color = map(int, input().split())

        # 파이썬은 0부터 시작이므로 1씩빼준다.
        i -= 1
        k -= 1

        # 돌을 넣어줌
        arr[i][k] = color

        # 8방향이기때문에 range(8)
        change = []

        for j in range(8):
            # 8방향에 해당하는 배열은 위에 만들어두었고 하나씩 해봄
            # 우측, 좌측, 상단, 하단, 우상단, 우하단, 좌상단, 좌하단
            ti = i + dx[j]
            tk = k + dy[j]
            # 방향을 움직일때 판을 넘어가면 중지
            change_8 =[]
            while 0 <= ti <N and 0 <= tk < N:
                # 첫번째 조건 움직였을때 지금이 W면 B이고 B였으면 W를 찾기
                if arr[ti][tk] != 0 and arr[ti][tk] != color:

                    change_8.append([ti, tk])
                    ti += dx[j]
                    tk += dy[j]

                # 두번째 조건 그러다가 0을 만나면 사이에 있는것이 아니기 때문에 break
                elif arr[ti][tk] == 0:
                    break

                # 세번째 조건 자기 색에 도착하면 사이에 있는것을 찾았기 때문에 좌표를 저장후
                # break
                else:
                    change.extend(change_8)
                    break

        # 저장된 좌표에 색을 칠해준다.
        for n in range(len(change)):
            x, y = change[n]
            arr[x][y] = color

    # 마지막으로 흰색과 검은색을 세어준다.
    count_w = 0
    count_b = 0
    for i in range(N):
        for k in range(N):
            if arr[i][k] == 1:
                count_b += 1
            elif arr[i][k] == 2:
                count_w += 1

    print('#{} {} {}'.format(test_case, count_b, count_w))



