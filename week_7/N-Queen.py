'''
* 유형
    백트랙

* 체감 난이도
    ***+

'''

def solution(n):
    global answer
    answer = 0
    diag1 = [i for i in range(2 * n - 1)]
    diag2 = [i for i in range(-n + 1, n)]
    pos = [i for i in range(n)]

    def recur(r, c):
        global answer

        if r == n - 1:
            answer += 1
            return

        try:
            pos.remove(c)
            diag1.remove(r + c)
            diag2.remove(r - c)
        except:
            pass

        for i in range(n):
            if i in pos and (r + 1 + i) in diag1 and (r + 1 - i) in diag2:
                recur(r + 1, i)

        pos.append(c)
        diag1.append(r + c)
        diag2.append(r - c)

    recur(-1, -1)
    return answer