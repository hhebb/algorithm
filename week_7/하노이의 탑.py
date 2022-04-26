''''
* 유형
    재귀 설계
    
* 체감 난이도
    ***
'''

def solution(n):
    global answer
    answer = []

    def recur(a, b, i):
        global answer

        if i == 1:
            answer.append([a, b])
            return

        c = 6 - (a + b)

        recur(a, c, i - 1)
        answer.append([a, b])
        recur(c, b, i - 1)

    recur(1, 3, n)
    return answer