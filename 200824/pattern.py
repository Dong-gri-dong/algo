def brute(t, p):
    i, j = 0, 0
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
        return i - len(p)
    else:
        return -1

text = "TTTTTAACCA"
pattern = "TTA"

print(brute(text, pattern))