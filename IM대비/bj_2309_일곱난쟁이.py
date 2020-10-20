import sys
sys.stdin = open("input_data/bj_2309")



def ki(k, sums, H):
    global flag
    if flag:
        return
    if sums > 100:
        return
    if k == 7:
        if sums == 100:
            flag = sorted(H)
            return
        return
    else:
        for i in range(9):
            if visit[i] == 0:
                visit[i] = 1
                ki(k+1, sums + h[i], H + [h[i]])
                visit[i] = 0

h = [int(input()) for _ in range(9)]
visit = [0] * 9
flag = False
ki(0, 0, [])
for i in flag:
    print(i)