def brute(t, p):
    i, j = 0, 0
    result = 0
    while j < len(p) and i < len(t):
        # j는 패턴의 index
        # i는 전체 텍스트의 index를 의미
        # 처음에는 둘다 0으로 시작
        if t[i] != p[j]:
            # 만약에 틀리다면
            # 지금 증가한 인덱스를 처음으로 돌리기 위해
            i = i - j # i와 j를 빼줌
            j = -1 # 그리고 이거는 j를 0으로 돌리기 위한것


        # 맞을때 마다 둘다 하나씩 올라감
        # 그리고 틀렸을 경우에는 j는 -1이여서 다시 0이 되고
        # i는 틀릴때마다 검사한 횟수 마다 +1이된다.
        i += 1
        j += 1

    if j == len(p):
        result = 1
        return result#i - len(p)
    else:
        return result



def boi(t, p):

    result = 0
    s = pattern[::-1]
    i = len(pattern)-1

    while i < len(text):
        nxt = len(s)
        j = 0
        if s[j] == text[i]:
            while j < len(s):
                if s[j] != text[i-j]:
                    break
                j += 1
            if j == len(s):
                result = 1

        else:
            while j < len(s):
                if s[j] == text[i]:
                    nxt = min(j, nxt)
                    break
                j += 1
        if result:
            break
        i += nxt

    return result



def brute(text, pattern):
    i = 0
    j = 0
    result = 0
    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            i = i - j
            j = -1

        i += 1
        j += 1
    if j == len(pattern):
        result = 1
        return result
    else:
        return result


def brute(text, pattern):
    i = 0
    j = 0
    result = 0
    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == len(pattern):
        result = 1
        return result
    return result



text = 'a pattern matching algorithm'
pattern = 'rithm'

print(brute(text, pattern))
# print(kmp(text, pattern))
#print(boi(text, pattern))