import sys

sys.stdin = open("input_data/4866.txt")


T = int(input())

for test_case in range(1, T +1):
    N = input()


    a = []

    result = 1

    for i in N:

        if i == '(' or i == '{':
            a.append(i)

        elif len(a) == 0 and i == ')' or len(a) == 0 and i == '}' :
            result = 0
            break

        elif len(a) != 0:
            if i == '}':
                if a[-1] == '{':
                    a.pop()
                else:
                    result = 0
                    break

            elif i == ')':
                if a[-1] == '(':
                    a.pop()
                else:
                    result = 0
                    break

    if a:
        result = 0


    print('#{} {}'.format(test_case, result))
