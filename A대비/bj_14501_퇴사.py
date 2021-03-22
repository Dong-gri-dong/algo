import sys
sys.stdin = open("./input_data/bj_14501_퇴사")

N = int(input())

temp = [list(map(int, input().split())) for _ in range(N)]

days = [0]
money = [0]
for i in range(N):
    days.append(temp[i][0])
    money.append(temp[i][1])

maxs = 0
def total_money(k, maxs_money):

    global maxs
    if k > N+1:
        return
    if k == N+1:
        if maxs <= maxs_money:
            maxs = maxs_money
        return
    if k == N:
        if days[k] == 1:
            maxs_money += money[k]
        if maxs <= maxs_money:
            maxs = maxs_money
        return
    else:
        total_money(k+days[k], maxs_money+money[k])
        total_money(k + 1, maxs_money)



total_money(1, 0)
print(maxs)

