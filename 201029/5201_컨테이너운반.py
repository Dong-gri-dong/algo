import sys
sys.stdin = open("input_data/5201_컨테이너운반.txt")


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    w = map(int, input().split())
    t = map(int, input().split())

    w = sorted(w)[::-1]
    t = sorted(t)[::-1]

    k = 0
    result = 0
    for i in t:
        for j in range(k, N):
            if i >= w[j]:
                result += w[j]
                k = j+1
                break

    print('#{} {}'.format(test_case, result))



