import sys

sys.stdin = open("input_data/1244_최대상금.txt")

T = int(input())

T = 1

for test_case in range(1, T+1):
    arrs, N = input().split()
    N = int(N)
    arrs = list(arrs)
    visit = {}

    def money(k, N):
        global result
        if k == N:
            result = max(result,  int(''.join(arrs)))
            return
        else:
            for i in range(0, len(arrs)):
                for j in range(i+1, len(arrs)):
                    if i != j:
                        arrs[i], arrs[j] = arrs[j], arrs[i]
                        temp = ''.join(arrs)
                        if visit.get((temp, k), 1):
                            print(visit)
                            visit[(temp, k)] = 0

                            money(k+1, N)
                        arrs[i], arrs[j] = arrs[j], arrs[i]




    result = 0
    money(0, N)
    print('#{} {}'.format(test_case, result))





