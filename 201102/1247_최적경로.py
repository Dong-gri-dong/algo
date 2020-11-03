import sys
sys.stdin = open("input_data/1247_최적경로.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arrs = list(map(int, input().split()))
    G = []
    for i in range(N+2):
        G.append([arrs[2*i], arrs[2*i+1]])

    def dis(arr_1, arr_2):
        d = abs(arr_1[0] - arr_2[0]) + abs(arr_1[1] - arr_2[1])
        return d



    visit = [0]*(N+2)
    def dist(k, result, pre):
        global results

        if results < result:
            return

        if k == N:
            result = result + dis(G[1], G[pre])
            if results >= result:
                results = result
            return
        else:
            for i in range(2, len(G)):
                if visit[i] == 0:
                    visit[i] = 1
                    dist(k+1, result+dis(G[i], G[pre]), i)
                    visit[i] = 0

    results = 21312738127391
    dist(0, 0, 0)
    print('#{} {}'.format(test_case, results))