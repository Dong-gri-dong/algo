import random

arrs = ['권용수',
        '김순석',
        '김윤빈',
        '남현준',
        '박대현',
        '박수빈',
        '박지영',
        '신동현',
        '윤기현',
        '이아영',
        '최동식']

random_list = random.sample(arrs, len(arrs))

print(random_list)