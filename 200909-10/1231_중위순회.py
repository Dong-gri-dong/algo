import sys
sys.stdin = open("input_data/1231.txt")


def inorder(v):
    global result
    if v == 0:
        return
    inorder(T[v][0])
    result += my_dict[str(v)]
    inorder(T[v][1])
for test_case in range(1, 10+1):
    N = int(input())
    temp = [list(input().split()) for _ in range(N)]


    my_dict = dict()

    T = [[0, 0, 0] for _ in range(N+1)]



    for i in range(N):
        p, d = temp[i][0], temp[i][1]
        my_dict[p] = d
        if len(temp[i]) >= 3:
            c = temp[i][2:]
        p = int(p)
        for k in c:
            k = int(k)
            if T[p][0] == 0:
                T[p][0] = k
            else:
                T[p][1] = k
            T[k][2] = p
        c =[]



    result = ''
    inorder(1)
    print('#{} {}'.format(test_case, result))

