import sys
import pprint
sys.stdin = open('input_data/4864.txt')

T = int(input())

for t in range(1, 1+T):
    pattern = input()
    text = input()

    i = 0
    j = 0
    result = 0
    while j < len(pattern) and i < len(text):
        if pattern[j] != text[i]:
            i = i - j
            j = -1

        i += 1
        j += 1

    if j == len(pattern):
        result = 1
    else:
        result = 0

    print("#{} {}".format(t, result))
