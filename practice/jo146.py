n = int(input())


count_num=0
count_alpha=0
alph=['A', 'B', 'C', 'D', 'E', 'F',
      'G', 'H', 'I', 'J', 'K', 'L',
      'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'X',
      'Y', 'Z']
u = n
for i in range(0, n):
    result = ''
    for k in range(n):
        if k < u-i:
            result += '{} '.format(alph[count_alpha])
            count_alpha += 1
        else:
            result += '{} '.format(count_num)
            count_num += 1
    print(result)
