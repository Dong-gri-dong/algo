import sys
import pprint
sys.stdin = open('input_data/1974.txt')

T = int(input())


def sort_func(y):
    x = y[:]
    for i in range(len(x)-1, 0 , -1):
        for j in range(0, i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x
for test_case in range(1, T + 1):
    result = 1
    N = [list(map(int, input().split())) for i in range(9)]


    # 가로 검증
    for i in range(9):
        stock_num = 1
        for k in sort_func(N[i]):
            if k == stock_num:
                stock_num += 1
            else:
                result = 0
                break


    # 세로 검증
    for i in range(9):
        stock_y = []
        for j in range(9):
            stock_y.append(N[j][i])
        stock_num = 1
        for k in sort_func(stock_y):
            if k == stock_num:
                stock_num += 1
            else:
                result = 0
                break

    # 3x3 검증
    for i in range(0, 3):

        for j in range(0, 3):
            stock_33 = []
            stock_33.extend(N[3*i][3*j:3*j + 3])
            stock_33.extend(N[3*i+1][3*j:3*j + 3])
            stock_33.extend(N[3*i+2][3*j:3*j + 3])
            stock_num = 1
            for k in sort_func(stock_33):

                if k == stock_num:
                    stock_num += 1
                else:
                    result = 0
                    break
    print('#{} {}'.format(test_case, result))