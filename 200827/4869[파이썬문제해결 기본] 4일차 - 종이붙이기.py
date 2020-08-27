import sys

sys.stdin = open("input_data/4869.txt")


def sq(n):
    if n == 1:
        return n
    elif n == 2:
        return 3
    else:
        return sq(n-1) + 2*sq(n-2)



T = int(input())

for test_case in range(1, T +1):
    N = int(input())

    result = 0
    a = N // 10

    result = sq(a)


    print('#{} {}'.format(test_case, result))
