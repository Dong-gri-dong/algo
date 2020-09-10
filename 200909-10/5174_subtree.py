import sys
sys.stdin = open("input_data/5174.txt")

T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))

    T = [[0, 0, 0] for _ in range(E+2)]

    for i in range(E):
        p, c = temp[2*i], temp[2*i+1]
        if T[p][0] == 0:
            T[p][0] = c
        else:
            T[p][1] = c
        T[c][2] = p



    def subnode(v):
        global count
        if v == 0:
            return
        count += 1
        subnode(T[v][0])
        subnode(T[v][1])

    count = 0
    subnode(N)
    print('#{} {}'.format(test_case, count))
