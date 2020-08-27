import sys

sys.stdin = open("input_data/4871.txt")


def dfs(v):
    visted[v] = 1
    global end
    global flag
    if v == end:
        flag = True
        return

    for w in range(1, V + 1):
        if G[v][w] == 1 and visted[w] == 0:
            dfs(w)



T = int(input())

for test_case in range(1, T +1):
    result = 0
    V, E = map(int, input().split())

    visted = [0]* (V+1)
    G = [[0] * (V+1) for _ in range(V+1)]

    temp = []
    for _ in range(E):
        temp.extend(list(map(int, input().split())))

    start, end = map(int, input().split())

    for i in range(E):
        s, e = temp[2*i], temp[2*i+1]
        G[s][e] = 1

    ### 재귀 함수 ###
    flag = False
    dfs(start)
    if flag:
        result = 1

    ### 반복 ###
    # S = [start]
    # visted[start] = 1
    # v = start
    # while S:
    #     if v == end:
    #         result = 1
    #         break
    #
    #     for w in range(1, V+1):
    #         if G[v][w] == 1 and visted[w] == 0:
    #             visted[w] = 1
    #             S.append(v)
    #             v = w
    #             break
    #
    #     else:
    #         v = S.pop()



    print('#{} {}'.format(test_case, result))
