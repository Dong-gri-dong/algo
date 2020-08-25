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



def get_pi(pattern):
    m = len(pattern)   # 패턴 크기를 담고
    pi = list(range(m)) # 패턴의 크기만큼의 pi배열을 만드는데 여기 담길꺼는
    #pi = [0]*m         # 글자가 하나씩 증가할때마다 겹치는 숫자   aba 라면 pi[2] = 1 aabaa이면 pi[5] == 2
    pi[1] = 0
    k = 0 # k값 초기화

    for q in range(2, m):
        #print(q)
        while(k > 0 and pattern[k] != pattern[q]):
            k = pi[k]
        if(pattern[k] == pattern[q]):
            k = k+1

        pi[q]=k


        #print(pi)
    return pi

print(get_pi('AAAABBA'))


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    # pi=[0]*n;
    pi = get_pi(pattern)
    q = -1
    for i in range(n):
        while (q > 0 and pattern[q] != text[i]):
            q = pi[q]
        if (pattern[q] == text[i]):
            q = q + 1
        if (q == m):
            print("pattern occurs with shift " + str(i - m))
            q = pi[q]







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










text = 'a pattern matching algorithm'
pattern = 'rithm'

# print(brute(text, pattern))
# print(kmp(text, pattern))
# print(boi(text, pattern))