import sys
sys.stdin = open("input_data/5202_화물도크.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arrs = [list(map(int, input().split())) for _ in range(N)]

    #print(arrs)

    start = sorted(arrs, key = lambda x : x[0])
    end = sorted(arrs, key = lambda x : x[1])
    count = 0
    go = 0
    for i in end:
        if go <= i[0]:
            count += 1
            go = i[1]
    print('#{} {}'.format(test_case, count))



