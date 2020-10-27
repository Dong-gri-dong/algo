import sys
sys.stdin = open("input_data/암호코드스캔.txt")

T = int(input())
alpha_16 = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}
hidden2num = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9
}
T = 1
for test_case in range(1, T+1):
    final = []
    last = []
    N, M = map(int, input().split())

    arrs = [input() for _ in range(N)]

    codes = []
    for i in range(len(arrs)):
        for j in range(len(arrs[i])):
            if arrs[i][j] != '0':
                codes.append(arrs[i])
                break
    # 코드가 있는 줄을 담음
    codes = list(set(codes))
    total_num = len(codes)


    check_list =[]
    for code in codes:
        new_arr = ''
        for i in code:
            if i in alpha_16:
                new_arr += bin(alpha_16[i])[2:]
            else:
                temp = bin(int(i))[2:]
                while len(temp) < 4:
                    temp = '0'+ temp
                new_arr += temp
        check_list.append(new_arr)
    # 16진수를 2진수로 바꿔줌
    codes = check_list


    for i in range(total_num):
        start = 0
        end = 0
        for j in range(len(codes[i])):
            if codes[i][j] == '1':
                end = j
        for j in range(len(codes[i])):
            if codes[i][j] == '1':
                start = j
                break


        check_code = codes[i][start:end + 1]
        num = (len(check_code)//56)+1
        while len(check_code) < 56 * num:
            check_code = '0' + check_code


        checks = []
        temp = ''
        for j in range(0, len(check_code)):
            temp += check_code[j]
            if j % (7*num) == (7*num)-1:
                checks.append(temp)
                temp = ''


        hidden = []
        for i in range(len(checks)):
            count = 0
            now_num = 0
            temp = ''
            for j in range(len(checks[i])):
                #checks[i][j]
                if now_num == int(checks[i][j]):
                    count += 1
                    if j == (7*num)-1:
                        temp += str(count//num)
                else:
                    temp += str(count//num)
                    now_num = int(checks[i][j])
                    count = 1
                    if j == (7*num)-1:
                        temp += str(count//num)
            hidden.append(temp)

        final_num = []
        for i in hidden:
            final_num.append(hidden2num[i])

        a = 0
        b = 0
        for i in range(0, len(final_num)):
            if (i + 1) % 2:
                a += final_num[i]
            else:
                b += final_num[i]

        final.append(a * 3 + b)
        last.append(a+b)


    last_idx = []
    for i in range(len(final)):
        if not final[i] % 10:
            last_idx.append(i)
    result = 0
    for i in last_idx:
        result += last[i]
    print("#{} {}".format(test_case, result))