'''

* 유형
    그리디, 구현

* 체감 난이도
    ***

* 풀이

'''

from collections import Counter

def solution(a):
    answer = 0
    answer2 = 0
    c = Counter(a)
    c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))

    if len(a) < 2:
        return 0

    for m, c in c.items():
        answer = 0
        front, back = 0, 1

        if c < answer2:
            continue

        for i in range(len(a)):
            try:
                if (a[front] == m and a[back] != m) or (a[front] != m and a[back] == m):
                    answer += 2
                    front, back = back + 1, back + 2
                else:
                    back += 1
            except:
                pass
        if answer2 < answer:
            answer2 = answer

    return answer2