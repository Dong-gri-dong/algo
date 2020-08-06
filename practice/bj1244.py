import sys

sys.stdin = open('input_data/bj_1244.txt')


T = int(input())
switch = list(map(int, input().split()))
student_num = int(input())



for i in range(student_num):
    student = list(map(int, input().split()))

    if student[0] == 1: #남
        baesu = []
        for n in range(1, T+1):
            if n % student[1] == 0:
                if switch[n-1]:
                    switch[n-1] = 0
                else:
                    switch[n - 1] = 1

    elif student[0] == 2:  # 여
        student[1] -= 1
        u = 0

        result = True
        while result:

            if u == 0:
                if switch[student[1]]:
                    switch[student[1]] = 0
                else:
                    switch[student[1]] = 1

                u += 1
            else:

                if student[1]- u >= 0 and student[1] + u <= T-1:
                    if switch[student[1]-u] == switch[student[1]+u]:
                       if switch[student[1]-u]:
                           switch[student[1] - u] = 0
                           switch[student[1] + u] = 0
                           u += 1
                       else:
                           switch[student[1] - u] = 1
                           switch[student[1] + u] = 1
                           u += 1
                    else:
                        result = False

                else:
                    break

for i in range(len(switch)):
    if (i+1) % 20 == 0:
        print(switch[i], end = "\n")
    else:
        print(switch[i], end =' ')






