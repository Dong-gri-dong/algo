import sys
sys.stdin = open("input_data/5203_베이빈진게임.txt")


T = int(input())

for test_case in range(1, T+1):
    arrs = list(map(int, input().split()))

    one = []
    two = []


    def run_check(arr):
        for i in range(len(arr)):
            if len(arr)-1  >= i+2:
                check1 = arr[i + 2] - arr[i+1]
                check2 = arr[i + 1] - arr[i]
                if check1 == check2:
                    return 1
        else:
            return 0




    for i in range(len(arrs)):
        if i % 2:
            two.append(arrs[i])
            if run_check(two):
                print('#{} {}'.format(test_case, 2))
                continue
        else:
            one.append(arrs[i])
            if run_check(one):
                print('#{} {}'.format(test_case, 1))
                continue
    print(one)
    print(two)
    print()
    print('#{} {}'.format(test_case, 0))

