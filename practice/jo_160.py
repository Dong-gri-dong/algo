# n = list(map(int, input().split()))
#
# result = [0]*6
# for i in n:
#     result[i-1] += 1
#
# for idx, i in enumerate(result):
#     print('{} : {}'.format(idx+1, i ))
#

T = list(map(int, input().split()))

max_num = T[0]


for number in T:
    if number >= max_num:
        max_num = number

# T의 최대값만큼의 길이를 가진 배열을 생성한다.
a = [0] * (max_num)

# T에 담긴 숫자를 a의 인덱스로 활용하여 등장할 때마다 숫자를 1씩 더한다.
# 예를 들어 숫자 5가 T에 담겼을 경우 인덱스의 특성에 의해 -1을 한 a[4]부분에 1을 추가한다.
for k in range(0, len(T)):
    a[T[k]-1] += 1


# a의 각 요소는 해당 인덱스 + 1에 해당하는 숫자가 등장하는 횟수와 같으므로 앞에서 부터 형식에 맞추어 출력한다.
j = 0
for i in a:
    print('{} : {}'.format(j + 1, i))

    j += 1
print('6 : 0')