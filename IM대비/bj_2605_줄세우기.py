import sys
sys.stdin = open("input_data/bj_2605")


N = int(input())
arr = list(map(int, input().split()))

result=[]
for i in range(N):
    if arr[i] == 0:
        result.append(i+1)
    else:
        S = []
        for j in range(arr[i]):
            S.append(result.pop())
        result.append(i+1)
        result.extend(S[::-1])


for i in result:
    print(i, end=" ")