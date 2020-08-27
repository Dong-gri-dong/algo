import sys

sys.stdin = open("input_data/1218.txt")

T = 10


for test_case in range(1, T+1):
    n = int(input())
    arr = input()
    mydict = {'()': 0, '{}': 0, '[]': 0, '<>': 0}
    #arr = {'(' : 0, '{' : 1, '[':2, '<':3, ')', '}', ]
    result = 1
    for i in arr:
        if i == '(':
            mydict['()'] += 1
        elif i == ')':
            mydict['()'] -= 1

            if mydict['()'] < 0:
                result = 0
                break

        elif i == '{':
            mydict['{}'] += 1
        elif i == '}':
            mydict['{}'] -= 1
            if mydict['{}'] < 0:
                result = 0
                break


        elif i == '[':
            mydict['[]'] += 1
        elif i == ']':
            mydict['[]'] -= 1
            if mydict['[]'] < 0:
                result = 0
                break

        elif i == '<':
            mydict['<>'] += 1
        elif i == '>':
            mydict['<>'] -= 1
            if mydict['<>'] < 0:
                result = 0
                break

    for k in mydict.values():
        if k < 0:
            result = 0

            break
    print('#{} {}'.format(test_case, result))