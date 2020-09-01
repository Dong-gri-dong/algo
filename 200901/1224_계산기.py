import sys

sys.stdin = open("input_data/1224_계산기3.txt")
arr = ['+', '-', '*', '/', '(', ')']

icp = {
    '+' : 1, '-' : 1,
    '*' : 2, '/' : 2,
    '(' : 3, ')' : 5}

isp = {
    '+' : 1, '-' : 1,
    '*' : 2, '/' : 2,
    '(' : -100, ')' : 5}


for test_case in range(1,11):
    a = ''
    n = int(input())
    S = []

    #n = '(6+5*(2-8)/2)'
    for i in input():


        if i not in arr:
            a += i

        else:
            if len(S) == 0:
                S.append(i)

            elif i == ')':
                while S[-1] != '(':
                    a += S.pop()
                S.pop()

            elif icp[i] > isp[S[-1]]:
                S.append(i)

            else:

                while icp[i] <= isp[S[-1]]:
                    a += S.pop()
                    if len(S) == 0:
                        break
                if icp[i] >= isp[S[-1]] or len(S) == 0:
                    S.append(i)



    S = []
    for i in a:
        if i not in arr:
            S.append(i)
        else:
            a = int(S.pop(-1))
            b = int(S.pop(-1))
            if i == '+':
                S.append(int(b+a))
            elif i == '-':
                S.append(int(b-a))
            elif i == '*':
                S.append(int(b*a))
            elif i == '/':
                S.append(int(b/a))

    result = S[-1]

    print('#{} {}'.format(test_case, result))

