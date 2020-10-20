import numpy as np

f = open("input_data/values") # 파일 읽기

str_arrs =[] # 문자
num_arrs =[] # 숫자
while True:
    line = f.readline()
    if not line:
        break
    str_arrs.append(line[0])

#chr  숫자 -> 문자
#ord  문자 -> 숫자

for i in str_arrs:
    num_arrs.append(ord(i))


print(str_arrs)
print(num_arrs)
print(np.mean(num_arrs))
print(np.var(num_arrs))

k = 123
n = 456
print('k는 값은 {} 그리고 n의 값은{}'.format(k, n))

print(f'{k}')


