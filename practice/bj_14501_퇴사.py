import sys

sys.stdin = open("input_data/bj_14501")

N = int(input())

arr = []
arr.append([])
for i in range(N):
    arr.append(list(map(int, input().split())))



def money(k, N, M):
    if k == N+1:
        result.append(M)
        return
    else:
        for i in range(k, N+1):
            if N+1 >= i+arr[i][0]:
                money(i+arr[i][0], N, M+arr[i][1])

            else:
                money(i+1, N, M)
                return
result = []
money(1, N, 0)
print(max(result))
