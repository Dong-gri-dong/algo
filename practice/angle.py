import math

a = [0 , 0]
b = [-3,  3]

x = b[1] - a[1]
# b는 넣어야할 공 a는 흰공
y = b[0] - a[0]


a = math.degrees(abs(math.atan(y/x)))

if x > 0 and y < 0:
    print(a)

elif x > 0 and y > 0:
    print(a+90)

elif x < 0 and y > 0:
    print(a+180)

elif x < 0 and y < 0:
    print(a+270)



a = [0 , 0]
b = [3,  3]

x = b[1] - a[1]
y = b[0] - a[0]

a = math.degrees(abs(math.atan(y / x)))

if x > 0 and y < 0:
    print(a)

elif x > 0 and y > 0:
    print(a + 90)

elif x < 0 and y > 0:
    print(a + 180)

elif x < 0 and y < 0:
    print(a + 270)


a = [0, 0]
b = [3,  -3]

x = b[1] - a[1]
y = b[0] - a[0]


a = math.degrees(abs(math.atan(y / x)))

if x > 0 and y < 0:
    print(a)

elif x > 0 and y > 0:
    print(a + 90)

elif x < 0 and y > 0:
    print(a + 180)

elif x < 0 and y < 0:
    print(a + 270)


a = [0 , 0]
b = [-3,  -3]

x = b[1] - a[1]
y = b[0] - a[0]

a = math.degrees(abs(math.atan(y / x)))

if x > 0 and y < 0:
    print(a)

elif x > 0 and y > 0:
    print(a + 90)

elif x < 0 and y > 0:
    print(a + 180)

elif x < 0 and y < 0:
    print(a + 270)


if x > 0 and y < 0:
    # 그대로
    pass

elif x > 0 and y > 0:
    # +90도
    pass

elif x < 0 and y > 0:
    # +180도
    pass

elif x < 0 and y < 0:
    # +270도
    pass





if a[0] > b[0]:
    # 위 포켓 가능
    pass

    if b[1] < 126:

        if a[1] < b[1]:
            # 2번 3번
            pass
        elif a[1] > b[1]:
            # 1번
            pass

    elif b[1] > 126:
        if a[1] < b[1]:
            # 3번
            pass
        elif a[1] > b[1]:
            # 1번 2번
            pass

elif a[0] < b[0]:
    # 아래 포켓 가능
    pass
    if b[1] < 126:

        if a[1] < b[1]:
            # 5번 6번
            pass
        elif a[1] > b[1]:
            # 4번
            pass

    elif b[1] > 126:
        if a[1] < b[1]:
            # 6번
            pass
        elif a[1] > b[1]:
            # 4번 5번
            pass