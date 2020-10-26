
T = int(input()) # 테스트 케이스

def score(k, N, sums, skip, M, count):  # 돌 점수 계산하는 함수
    # k :지금위치, N: 끝, sums: 점수합을 담는 변수, skip: 스킵횟수를 세는것 , M: 몇번가지 돌밟는게 가능한지, count: 돌밟은 횟수
    if count > M: # 횟수가 넘어가면 리턴 가지치기
        return
    if k == N: # 끝까지 갔을때
        result.append(sums) #점수를 담아줌
        return
    if skip >= 2: # 스킵 두번했을때 리턴 가지치기 주석달기 쉽게 나눠놓음 위랑 합쳐도 됨
        return

    else:
        score(k + 1, N, sums + stone[k], 0, M, count + 1) #돌을 밟을때
        score(k + 1, N, sums, skip + 1, M, count) # 돌을 넘어갈때

for test_case in range(1, T+1):
    # N: 돌갯수
    # M: 밟는 횟수
    N, M = map(int,input().split())
    stone = list(map(int, input().split())) #돌점수

    result = [] # 결과 담을 배열
    score(0, N, 0, 0, M, 0) # 함수불러옴
    print('#{} {}'.format(test_case, max(result))) # 결과