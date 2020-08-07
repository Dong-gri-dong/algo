import sys
import pprint
sys.stdin = open('input_data/1258.txt')


def sort_func_2(y):
    x = y[:]
    for i in range(len(x) - 1, 0, -1):
        for j in range(0, i):
            if x[j][2] > x[j + 1][2]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x




def sort_func_0(y):
    x = y[:]
    for i in range(len(x) - 1, 0, -1):
        for j in range(0, i):
            if x[j][2] == x[j + 1][2]:
                if x[j][0] > x[j + 1][0]:
                    x[j], x[j + 1] = x[j + 1], x[j]
    return x

T = int(input())



for test_case in range(1, T + 1):
    real_final = ''
    final_lists = []
    N = int(input())

    lists = [list(map(int, input().split())) for i in range(N)]

    ### 리스트 출력 ###
    # pprint.pprint(lists)


    h = []
    for i in range(N):
        for k in range(N):
            if lists[i][k] != 0:
                h.append([i,k])

    # print('병이 있는 위치 {}'.format(h))


    while h:
        first = []
        # print('####')
        # print(h)
        # print('####')
        for i in range(len(h)):
            if not first: #리스트가 존재 안하면 첫번째 값 추가
                first.append(h[i]) # 0

            elif first: #리스트가 존재 하면 값들 추가
                if first[-1][0] == h[i][0] and first[-1][1] + 1 == h[i][1]:
                    first.append(h[i])
                else:
                    #for _ in range(len(first)):
                    #    h.remove(first[_])
                    break

        h_count = 1 #행의 크기
        first_value = first[0] # 행의 크기를 구하기위한 값
        last_value = first[-1]
        for i in range(len(h)):
            if last_value[0] + 1 == h[i][0] and last_value[1] == h[i][1]:
                h_count += 1
                last_value = h[i]
        # 이제 여기서 사각형의 준비다를 구함

        square_lists = []
        for i in range(first_value[0], last_value[0]+1):
            for j in range(first_value[1], last_value[1] + 1):
                square_lists.append([i, j])



        # print('사각형{} 윗변'.format(first))
        # print('병이 있는 위치 {}'.format(h))
        # print('지금 사각형 행 크기 {}'.format(h_count))
        # print('지금 사각형 좌상단 {}'.format(first_value))
        # print('지금 사각형 우하단 {}'.format(last_value))

        h_value = last_value[0] - first_value[0] + 1
        # print('행 크기 {}'.format(h_value))
        y_value = last_value[1] - first_value[1] + 1
        # print('열 크기 {}'.format(y_value))
        square_size = h_value*y_value
        # print('사각형 크기 {}'.format(square_size))
        # print('사각형 리스트 {}'.format(square_lists))


        for i in range(len(square_lists)):
           h.remove(square_lists[i])

        # print('사각형뺀 병 리스트 {}'.format(h))
        #


        final_lists.append([h_value, y_value, square_size])
    #     print('')
    #     print('')
    #
    # print('출력하기전 리스트 {}'.format(final_lists))


    final_lists = sort_func_0(sort_func_2(final_lists))

    real_final += '{} '.format(len(final_lists))
    for i in range(len(final_lists)):
        real_final += '{} {} '.format(final_lists[i][0], final_lists[i][1])
    print('#{} {}'.format(test_case, real_final))