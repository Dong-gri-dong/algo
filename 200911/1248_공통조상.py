import sys

sys.stdin = open("input_data/1248.txt")


def binary(n):
    global count
    if n == 0:
        return
    count += 1
    binary(T[n][0])
    binary(T[n][1])

def parents(n, S):
    global result
    if n == 1:
        result = S
        return

    parents(T[n][2], S + [T[n][2]])

T = int(input())
for test_case in range(1, T+1):
    V, E, v1, v2 = map(int, input().split())


    temp = list(map(int, input().split()))
    T = [[0, 0 ,0] for _ in range(V+1)]


    for i in range(E):
        p, c = temp[2*i], temp[2*i + 1]

        if T[p][0] == 0:
            T[p][0] = c
        else:
            T[p][1] = c
        T[c][2] = p

    parents(v1, [])
    result_v1 = result
    parents(v2, [])
    result_v2 = result

    LCA = 0
    for i in result_v1:
        for j in result_v2:
            if i == j:
                LCA = i
                break
        if LCA:
            break



    count = 0
    binary(LCA)

    print('#{} {} {}'.format(test_case, LCA, count))