import sys

sys.stdin = open("input_data/1220_magnetic.txt")

# 1 : N극  1과 멀어짐 2이 붙음
# 2 : S극  2와 멀어짐 1이 붙음
# 위가 N극 아래가 S극


# 아래방향
dx = [0]
dy = [1]

### 다 상태를 바꾼후 dfs로 하고 싶었는데 실패 나중에 해보고 싶음
# for test_case in range(1, 11):
#
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#
#
#     count = 1
#     while count != 0:
#         count = 0
#         for i in range(N-1, -1, -1):
#             for k in range(N):
#
#                 if arr[i][k] == 1: #N극 아래로 가야함
#                     if i+1 == N:
#                         arr[i][k] = 0
#                         count += 1
#                     else:
#                         if arr[i + 1][k] == 0:
#
#                             arr[i][k], arr[i + 1][k] = arr[i + 1][k], arr[i][k]
#                             count += 1
#         for i in range(N):
#             for k in range(N):
#                 if arr[i][k] == 2:# S극 위로 가야함
#                     if i == 0:
#                         arr[i][k] = 0
#                         count += 1
#                     else:
#                         if arr[i -1][k] == 0:
#                             arr[i][k], arr[i - 1][k] = arr[i - 1][k], arr[i][k]
#                             count += 1
#
#
#
#
#
#
#
#     result = 0
#
#     for i in range(N):
#         for k in range(N):
#             flag = False
#
#             if visited[i][k] == 1 or arr[i][k] != 1:
#                 continue
#
#             S = [[i , k]]
#             visited[i][k] = 1
#
#             while S:
#
#                 if flag:
#                     result += 1
#                     break
#
#                 for u in range(0,1):
#                     ti = i + dy[u]
#                     tk = k + dx[u]
#
#                     if ti < 0 or ti == N or tk < 0 or tk == N:
#                         continue
#                     if arr[ti][tk] == 0  or visited[ti][tk] == 1:
#                         continue
#                     if arr[ti][tk] == 2:
#                         visited[ti][tk] = 1
#                         flag = True
#                         break
#                     visited[ti][tk] = 1
#                     S.append([ti, tk])
#                     i = ti
#                     k = tk
#                     break
#
#                 else:
#                     i, k = S.pop()
#             count = 0
#
#
#     print('#{} {}'.format(test_case, result))

# 1 : N극  1과 멀어짐 2이 붙음
# 2 : S극  2와 멀어짐 1이 붙음
# 위가 N극 아래가 S극
for test_case in range(1, 11):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for k in range(N):
        S = []
        for i in range(N):
            if arr[i][k] == 1:
                S.append(arr[i][k])
            if arr[i][k] == 2 and len(S) != 0:
                S = []
                count += 1


    print('#{} {}'.format(test_case, count))

