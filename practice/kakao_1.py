import sys
sys.stdin = open("input_data/kakao_1")

def solution(new_id):
    arr = ['-', '_', '.']
    answer =new_id.lower()
    answer = list(answer)[1:-1]


    result =''
    for i in answer:

        if not i.islower() and i not in arr and not i.isdigit():
            pass
        else:
            result += i
    answer = result

    #
    # count = 0
    # result = ''
    # for i in range(len(answer)):
    #     if answer[i] == '.':
    #         count += 1
    #     else:
    #         if count:
    #             result += '.'
    #         count = 0
    #         result += answer[i]
    # answer = result
    # answer = list(answer)
    #
    #
    # if answer:
    #     if answer[0] == '.':
    #         answer.pop(0)
    #     if answer[-1] == '.':
    #         answer.pop(-1)
    #
    # if len(answer) == 0:
    #     answer = 'a'
    #
    # answer = answer[0:15]
    #
    # if answer[-1] == '.':
    #     answer.pop(-1)
    #
    # answer = list(answer)
    # if len(answer) <= 2:
    #     while len(answer) <= 2:
    #         answer.append(answer[-1])
    # result =''
    # for i in answer:
    #     result += i
    # answer = ('"{}"'.format(result))
    return answer

T = int(input())


for i in range(1, T+1):
    print(solution(input()))