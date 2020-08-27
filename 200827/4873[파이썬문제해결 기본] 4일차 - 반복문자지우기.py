import sys

sys.stdin = open("input_data/4873.txt")





T = int(input())

for test_case in range(1, T +1):
    N = list(input())


    s = []
    for i in N:
        if not s:
            s.append(i)

        elif s[-1] == i:
            s.pop()
        else:
            s.append(i)






    print('#{} {}'.format(test_case, len(s)))
