import sys
sys.stdin = open("input_data/3499_퍼팩트셔플.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arrs = list(input().split())

    if len(arrs) % 2:
        arr_1 = arrs[0: (N // 2) + 1]
        arr_2 = arrs[(N // 2) + 1:]
    else:
        arr_1 = arrs[0: (N//2)]
        arr_2 = arrs[(N // 2):]
    a = len(arr_1)
    b = len(arr_2)

    result = []
    j = 0
    while j <= N//2:
        if a >= j+1:
            result.append(arr_1[j])
        if b >= j+1:

            result.append(arr_2[j])
        j += 1


    print('#{}'.format(test_case), end='')
    for i in result:
         print(' {}'.format(i), end='')
    print()
