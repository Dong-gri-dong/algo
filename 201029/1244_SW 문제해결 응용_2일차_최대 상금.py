import sys
sys.stdin = open("input_data/1244_SW 문제해결 응용_2일차_최대 상금.txt")

T = int(input())
T = 1
for test_case in range(1, T+1):
    arrs, N = (input().split())
    N = int(N)
    arrs = list(arrs)
    print(arrs)



    N = int(N)

    result = []
    def money(k, N):
        if k == N:
            result.append(arrs)
            return

        else:
            for i in range(0, 3):
                arrs[i], arrs[k] = arrs[k], arrs[i]
                money(k+1, N)
                arrs[i], arrs[k] = arrs[k], arrs[i]

    money(0, N)
    print(result)
