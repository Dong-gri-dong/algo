import sys

sys.stdin = open("input_data/10888.txt")

T = int(input())


def dists(x, y):
    return abs(y[0] - x[0]) + abs(y[1] - x[1])


for test_case in range(1, T+1):
    N = int(input())

    arrs = [list(map(int, input().split())) for _ in range(N)]


    house = []
    food = []
    food_value = []
    for y in range(N):
        for x in range(N):
            if arrs[y][x] == 1:
                house.append([y, x])
            if arrs[y][x] > 1:
                food.append(([y, x]))
                food_value.append(arrs[y][x])

    A = [0] * len(food)





    power_set = []
    def powerset(n, k):

        if n == k:
            sums = []
            for i in range(n):
                if A[i]:
                    sums.append(i)
            power_set.append(sums)

        else:
            # k번째 선택
            A[k] = 1
            powerset(n, k + 1)
            # k번째 비선택
            A[k] = 0
            powerset(n, k + 1)

    powerset(len(food), 0)


    set_num = [[] for _ in range(len(food))]

    for i in range(1, len(food)+1):
        for j in power_set:
            if i == len(j):
                set_num[i-1].append(j)


    dist = []
    for i in house:
        a=[]
        for j in food:
            a.append(dists(i, j))

        dist.append(a)



    result = []

    for n in range(len(food_value)):

        for j in set_num[n]:
            sums = 0
            for i in range(len(dist)):
                temp = []
                for k in j:
                    if i == 0:
                        sums += food_value[k]
                    temp.append(dist[i][k])

                sums += min(temp)

            result.append(sums)





    print('#{} {}'.format(test_case, min(result)))





