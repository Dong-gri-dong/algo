import sys

sys.stdin = open('input_data/4839.txt')


T = int(input())

for t in range(1, T + 1):
    total, A, B = list(map(int, input().split()))

    result_A = 0
    result_B = 0
    result = 0
    start_A = 1
    start_B = 1
    end_A = total
    end_B = total

    i = 0
    while start_A < end_A  or start_B < end_B:

        middle_A = int((start_A + end_A) / 2)
        middle_B = int((start_B + end_B) / 2)

        if middle_A == A:
            result_A = 'A'
        elif middle_A > A:
            end_A = middle_A
        else:
            start_A = middle_A

        if middle_B == B:
            result_B = 'B'
        elif middle_B > B:
            end_B = middle_B
        else:
            start_B = middle_B

        if result_A == 'A' or result_B == 'B':
            break
        i+=1

    if result_A:
        if result_B:
            result = 0
        else:
            result = result_A
    elif result_B:
        if result_A:
            result = 0
        else:
            result = result_B


    print('#{} {}'.format(t, result))


