'''
* 유형
    구현

* 체감난이도
    **

* 풀이


'''

def solution(s):
    answer = 0
    s_copy = s[:]

    for ii in range(len(s_copy)):
        s = s_copy[ii:]
        length = 0
        for i in range(len(s)):
            # 짝 일땐 문자가 기준
            if i % 2 == 0:
                t = i // 2
                a = s[:t]
                m = s[t]
                b = s[t + 1:t + 1 + len(a)][::-1]
                if a == b:
                    length = (t) * 2 + 1
            # 홀 일땐 문자 사이가 기준.
            else:
                t = i // 2
                m = s[t], s[t + 1]
                a = s[:t]
                b = s[t + 2:t + 2 + len(a)][::-1]
                if m[0] == m[1] and a == b:
                    length = (t) * 2 + 2

        if answer < length:
            answer = length
    return answer