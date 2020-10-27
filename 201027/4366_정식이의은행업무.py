import sys
sys.stdin = open("input_data/4366_정식이의은행업무.txt")

T = int(input())

for test_case in range(1, T+1):
    binary = input()
    ternary = input()
    possible_binary = [binary]
    possible_ternary = [ternary]

    binary = list(binary)
    ternary = list(ternary)



    j = 0
    while j < len(binary):
        temp = binary[:]

        if temp[j] == '0':

            temp[j] = 1
        else:

            temp[j] = 0

        x = ''
        for i in temp:
            x += str(i)
        possible_binary.append(x)
        j += 1



    j = 0
    while j < len(ternary):
        temp_1 = ternary[:]
        temp_2 = ternary[:]
        if temp_1[j] == '0':
            temp_1[j] = 1
            temp_2[j] = 2
        elif temp_1[j] == '1':
            temp_1[j] = 0
            temp_2[j] = 2
        else:
            temp_1[j] = 0
            temp_2[j] = 1

        x = ''
        for i in temp_1:
            x += str(i)
        possible_ternary.append(x)
        x = ''
        for i in temp_2:
            x += str(i)
        possible_ternary.append(x)
        j += 1

    check_ternary = []
    for i in possible_ternary:
        check_ternary.append(int(i, 3))

    check_binary = []
    for i in possible_binary:
        check_binary.append(int(i, 2))

    for i in check_binary:
        if i in check_ternary:
            print('#{} {}'.format(test_case, i))
            break