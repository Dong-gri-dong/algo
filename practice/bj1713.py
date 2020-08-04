import sys

sys.stdin = open('input_data/bj_1713.txt')

N = int(input())
T = int(input())

num = list(map(int, input().split()))

result = []
for i in range(T):
    if len(result) >= N:
        older = result[0][1]
        for i in range(N):
            if older <= result[i][1]:
                older = result[i][1]
                print(i)
            #print(older)

        result.append([num[i], i])

    else:
        result.append([num[i], i])

#print(result)


