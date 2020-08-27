import sys

sys.stdin = open("input_data/1219.txt")

# T = 10
# for test_case in range(1, T+1):
#
#     # 1. 먼저 노드 수 엣지 수 그리고 그래프 연결정보등을 다 받는다.
#     _, E = map(int, input().split())
#     N = 100
#     temp = list(map(int, input().split()))
#
#
#     # 2. 그래프와 visted를 만들어준다. 노드 수 기준으로
#     G = [[0] * (N) for _ in range(N)]
#     visited = [0] * N
#
#
#     # 3. 그리고  인접 행렬을 만들어준다.
#     for i in range(E):
#         s, e = temp[2*i], temp[2*i+1]
#         G[s][e] = 1
#     result = 0
#
#
#     flag = False # 도중에 행렬을 만들수 있는 변수
#
#     def dfs(v):
#         global flag
#         if flag:
#             return
#
#         visited[v] = 1 # 방문 했다 표시
#
#         # 인접한 노드를 찾기 위해서
#         for w in range(0, N):
#             # 인접한 행렬이 있고 방문한적이 없다면
#             if G[v][w] == 1 and visited[w] == 0:
#
#                 # 조건에 맞쳐서 조건이 맞다면 flag를 True로
#                 if w == 99:
#                     flag = True
#                 # 아닌 경우에 다음 경로에서 dfs적용
#                 else:
#                     dfs(w)
#
#     dfs(0)
#     if flag:
#         result = 1
#     print('#{} {}'.format(test_case, result))






T = 10

for test_case in range(1, T+1):

    _, E = map(int, input().split())
    temp = list(map(int, input().split()))
    N = 100
    # # index를 위해 1 크게
    # # 인접 행렬
    G = [[0] * (N) for _ in range(N)]
    # # 방문 체크
    visit =[0] * (N)

    for i in range(0, E*2, 2):
        s, e = temp[i], temp[i+1]
        G[s][e] = 1

    # 시작점을 방문하고 스택에 push
    # S = [0]
    # visit[0] = 1
    # v = 0     # v = 현재 방문하는 정점
    # paths = []
    # result = 0
    # while S:  # 빈 스택이 아닐 동안 반복
    #     # v의 방문하지 않은 인접정접을 찾는다.
    #     # v의 인접정점은 G[v]
    #
    #     if v == 99:
    #         result = 1
    #         break
    #
    #     for w in range(0, N):
    #         if G[v][w] == 1 and visit[w] == 0:
    #             # v ---> w
    #             visit[w] = 1; #print(w, end = ' ')
    #             S.append(v)
    #             v = w
    #             break
    #     # for else 구문은 for문에있는 break가 걸리면 else가 실행안되지만
    #     # break안걸리면 else 실행
    #     else:
    #         v = S.pop()
    # print('#{} {}'.format(test_case, result))


# 1. 스택에 첫 노드를 넣고 방문기록에도 남기고 내 위치도 옮김
    S = [0]
    visit[0] = 1
    v = 0
    result = 0
    while S:

        for w in range(0, N):
            if G[v][w] == 1 and visit[w] == 0:

                visit[w] = 1
                S.append(v)
                v = w
                if v == 99:
                    result = 1

                break
        else:
            v = S.pop()


    print('#{} {}'.format(test_case, result))









