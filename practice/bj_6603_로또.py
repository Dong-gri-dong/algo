import sys
sys.stdin = open("input_data/bj_6603")


def lotto(k, N, lo):
    global count
    if k == 6:
        lo = sorted(lo)
        if lo not in result:
            result.append(lo)
        return
    else:
        for i in range(k, N):
            if visit[i] == 0:
                visit[i] = 1
                lotto(k + 1, N, lo + [S[i]])
                visit[i] = 0


while True:
    arr = input()
    if arr == '0':
        break


    arr = list(map(int, arr.split()))

    N = arr[0]
    S = arr[1:]
    visit = [0] * N

    result = list()
    count = 0
    lotto(0, N, [])

    for i in result:
        for j in i:
            print(j, end = ' ')
        print()
    print()
