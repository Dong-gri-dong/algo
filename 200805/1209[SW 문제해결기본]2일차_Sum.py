import sys

sys.stdin = open('input_data/1209.txt')

T = 10

for t in range(1, T + 1):
    result = []
    N = int(input())
    mylist = [list(map(int, input().split())) for _ in range(100)]

    for i in range(len(mylist)):
        sums_1 = 0
        sums_2 = 0
        sums_3 = 0
        sums_4 = 0
        for n in range(len(mylist)):
            sums_1 += mylist[i][n]
            sums_2 += mylist[n][i]
            if i == n:
                sums_3 += mylist[i][n]
            if i + n == len(mylist)-1:
                sums_4 += mylist[i][n]

        result.append(sums_1)
        result.append(sums_2)
        result.append(sums_3)
        result.append(sums_4)
    #print('#{} {}'.format(t, max(result)))

    max_result = result[0]
    for i in range(len(result)):
        if max_result < result[i]:
            max_result = result[i]
    print('#{} {}'.format(t, max_result))



