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
    new_codes = []
    for code in codes[100:101]:

        count = 0
        temp = ''
        for i in code:
            if i != '0' and count > 5:
                new_codes.append(temp)
                temp =''
                count = 0
            elif i == '0':
                count += 1
            elif i != '0':
                count = 0
            temp += i

        codes = new_codes
        new_codes =[]

        for code in codes:
            for i in range(1, len(code)):
                if code[-i] != '0':
                    new_codes.append(code[:(len(code)-i)+1])
                    break


        codes = new_codes

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
        new_codes =[]


        for code in codes:
            for i in range(1, len(code)):
                if code[-i] != '0':
                    new_codes.append(code[:(len(code)-i)+1])
                    break


        codes = new_codes


        for code in codes:
            print(code)
            print()
            for i in range(1,8):
                if i == 1:
                    print(code[-7 * i:])
                else:
                    print(code[-7*i:-7*(i-1)])


