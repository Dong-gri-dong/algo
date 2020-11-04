import sys

sys.stdin = open("input_data/14889_스타트와링크")


N = int(input())
arrs = [list(map(int, input().split())) for _ in range(N)]

def score(x):
    s = 0
    for i in range(len(x)):
        for j in range(0, len(x)):
            s += arrs[x[i]][x[j]]
    return s

def soccer(k, start, link):
    global result

    if len(start)> N//2 or len(link) > N//2:
        return
    if k == N:
        if start in check:
            return
        else:
            check.append(start)
            temp = abs(score(start)-score(link))
            if result >= temp:
                result = temp
            return
    else:

        soccer(k + 1, start + [k], link)
        soccer(k + 1, start, link + [k])



result = 123124151231
check = []
s = []
l = []

soccer(0, [], [])

print(result)