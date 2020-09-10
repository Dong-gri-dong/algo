import sys

sys.stdin = open("input_data/1232.txt")



for test_case in range(1, 10+1):
    N = int(input())

    T = [[0, 0, 0] for _ in range(1+N)]
    temp = [list(input().split()) for _ in range(N)]

    my_dict = dict()
    for i in range(N):
        if len(temp[i]) > 2:
            p, d = temp[i][0], temp[i][1]
            c = temp[i][2:]
            p = int(p)
            for j in c:
                j = int(j)
                if T[p][0] == 0:
                    T[p][0] = j
                else:
                    T[p][1] = j
                T[j][2] = p
            my_dict[str(p)] = d
        else:
            p, c = temp[i][0], int(temp[i][1])
            my_dict[p] = int(c)



    def order(v):
        global result
        if v == 0:
            return

        order(T[v][0])
        order(T[v][1])
        result.append(str(v))

    result = []
    order(1)

    arr = ['-', '+', '*', '/']
    S = []




    for i in result:
        if my_dict[i] in arr:
            if my_dict[i] == '-':
                b = S.pop()
                a = S.pop()
                S.append(a - b)
            elif my_dict[i] == '+':
                b = S.pop()
                a = S.pop()
                S.append(a + b)
            elif my_dict[i] == '*':
                b = S.pop()
                a = S.pop()
                S.append(a * b)
            elif my_dict[i] == '/':
                b = S.pop()
                a = S.pop()
                S.append(a / b)
        else:
            S.append(my_dict[i])

    print('#{} {}'.format(test_case, int(S[-1])))