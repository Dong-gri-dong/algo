import sys
import pprint

sys.stdin = open("input_data/1211.txt")




T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]


    j = []
    for i in range(100):
        if arr[0][i] == 1:
            j.append(i)

    mins = 999
    mins_idx = 0

    for k in j:
        start = k
        count = 0
        i = 0
        while i != 99:
            if k + 1 >= 100:
                while arr[i][k - 1] == 1:
                    k -= 1
                    count += 1
                i += 1
                count+=1

            elif k - 1 < 0:
                while arr[i][k + 1] == 1:
                    k += 1
                    count += 1
                i += 1
                count += 1
            else:
                if arr[i][k + 1] == 1:
                    k += 1
                    count += 1
                    while arr[i][k + 1] == 1:
                        k += 1
                        count += 1
                        if k == 99:
                            break
                    i += 1
                    count += 1
                elif arr[i][k - 1] == 1:
                    k -= 1
                    count += 1
                    while arr[i][k - 1] == 1:
                        k -= 1
                        count += 1
                        if k == 0:
                            break
                    i += 1
                    count += 1
                else:
                    i += 1
                    count += 1

        if count < mins:
            mins = count
            mins_idx = start
    print('#{} {}'.format(test_case, mins_idx))
