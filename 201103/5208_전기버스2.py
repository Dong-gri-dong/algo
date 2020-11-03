import sys
sys.stdin = open("input_data/5208_전기버스2.txt")

T = int(input())

for test_case in range(1, T+1):
    arrs = list(map(int, input().split()))

    N = arrs[0]



    def bus(k, bat, count):
        global result
        if result < count:
            return

        if k >= N:
            return
        else:
            for i in range(k+1, k+bat+1):
                bus(i, bat+arrs[i]-(k-i), count+1)




    result = N-1
    bus(1, arrs[1], 0)
    print('#{} {}'.format(test_case, result))

