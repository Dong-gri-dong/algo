import sys

sys.stdin = open("input_data/4874.txt")

T = int(input())
arr = ['+', '-', '*', '/']


for test_case in range(1, T+1):
    n = input().split()
    result = 0
    S = []
    for i in n:
        if i == '.':
            if len(S) > 1:
                result = 'error'
                break
            result = S[-1]

        elif i == '+':
            if len(S) < 2:
                result = 'error'
                break
            a = int(S.pop())
            b = int(S.pop())

            S.append(b + a)

        elif i == '-':
            if len(S) < 2:
                result = 'error'
                break
            a = int(S.pop())
            b = int(S.pop())

            S.append(b - a)

        elif i == '*':
            if len(S) < 2:
                result = 'error'
                break
            a = int(S.pop())
            b = int(S.pop())

            S.append(b * a)

        elif i == '/':
            if len(S) < 2:
                result = 'error'
                break
            elif a == 0:
                result = 'error'
                break
            a = int(S.pop())
            b = int(S.pop())

            S.append(int(b / a))

        else:
            S.append(i)

    print('#{} {}'.format(test_case, result))

