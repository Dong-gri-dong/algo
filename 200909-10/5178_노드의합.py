import sys

sys.stdin = open("input_data/5178.txt")


T = int(input())

for test_case in range(1, T+1):
    #N: 노드의 개수
    #M: 리프 노드의 개수
    #L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    T = [0] * (1+N)
    temp = [list(map(int, input().split())) for _ in range(M)]

    for i in range(M):
        idx, value = temp[i][0], temp[i][1]
        T[idx] = value



    for i in range(N, 1, -1):

        if T[i//2]:
            pass
        else:
            if (i // 2) * 2 <= N and (i // 2) * 2 + 1 <= N:
                T[i // 2] = T[(i // 2) * 2] + T[(i // 2) * 2 + 1]
            elif T[(i//2)*2]:
                T[i // 2] = T[(i // 2) * 2]
            #elif T[(i//2)*2+1]:
            #    T[i//2] = T[(i//2)*2+1]

    print('#{} {}'.format(test_case, T[L]))
