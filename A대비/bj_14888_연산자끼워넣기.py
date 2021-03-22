import sys
sys.stdin = open("input_data/bj_14888_연산자끼워넣기")

N = int(input())
arrs = list(map(int, input().split()))
math_sign = list(map(int, input().split()))



def find_max(k, value, sign):

    global maxs
    global mins
    if k == N:
        if maxs <= value:
            maxs = value
        if mins >= value:
            mins = value
        return
    else:
        for i in range(4):
            if sign[i] != 0:
                if i == 0:
                    sign[i] -= 1
                    find_max(k+1, value+arrs[k], sign)
                    sign[i] += 1
                elif i == 1:
                    sign[i] -= 1
                    find_max(k+1, value-arrs[k], sign)
                    sign[i] += 1
                elif i == 2:
                    sign[i] -= 1
                    find_max(k+1, value*arrs[k], sign)
                    sign[i] += 1
                elif i == 3:
                    sign[i] -= 1
                    if value < 0:
                        find_max(k+1, -(-value//arrs[k]), sign)
                    else:
                        find_max(k + 1, value // arrs[k], sign)
                    sign[i] += 1
mins = +10000000000
maxs = -10000000000
find_max(1, arrs[0], math_sign)
print(int(maxs))
print(int(mins))