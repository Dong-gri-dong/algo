content = '안녕안녕   #해시태그#연습'

hashs = []
if '#' in content:
    for i in range(len(content)):
        if content[i] == '#':
            check = content[i:]
            break
    for i in check.split('#'):
        if i:
            hashs.append('#{}'.format(i))
    print(hashs)


