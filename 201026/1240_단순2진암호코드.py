import sys
sys.stdin = open("input_data/1240_단순2진암호코드.txt")


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arrs = [list(map(int, input())) for _ in range(N)]

    for i in range(len(arrs)):
        for j in range(len(arrs[i])):
            if arrs[i][-j] == 1:
                temp_y = i
                temp_x_end = len(arrs[0])-j
                break
    temp_x_start = temp_x_end-56+1
    numbers = arrs[temp_y][temp_x_start:temp_x_end + 1]

    check_number = []
    temp = []
    for i in range(0, len(numbers)):
        temp.append(numbers[i])

        if i%7 == 6:
            check_number.append(temp)
            temp=[]

    hidden = []

    for j in range(0, len(check_number)):
        temp = ''
        num = 0
        count = 1
        for i in range(1, len(check_number[j])):

            if num == check_number[j][i]:
                count += 1
                if i == 6:
                    temp += str(count)
            else:
                num = check_number[j][i]
                temp += str(count)
                count = 1
                if i == 6:
                    temp += str(count)
        hidden.append(temp)


    final_num = []
    for i in hidden:

        final_num.append(hidden2num[i])

    a = 0
    b = 0
    for i in range(0, len(final_num)):
        if (i+1) % 2:
            a += final_num[i]
        else:
            b += final_num[i]



    if (a*3+b) % 10:
        print('#{} 0'.format(test_case))
    else:
        print('#{} {}'.format(test_case, sum(final_num)))