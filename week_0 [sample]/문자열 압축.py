'''
* 문제 유형: 단순 구현, 문자열 다루기

* 체감 난이도: ** (별 2 개)

* 풀이 1:
    ex) 문제 푸는데 사용한 아이디어.
    ex) 복잡한 문제의 경우 풀이 절차를 간략하게

* 주의할 점:
    ex) ~ 상황에서 인덱스 에러 날 가능성이 높음.
    ex) 루프 도는 중에 딕셔너리 사이즈가 변해서 에러 날 수 있음.
    등등

* 문법 팁:
    ex) 이중 리스트 표현식으로 코드 수를 줄일 수 있었다.

* 기타
    ex) ~ 내장함수를 썼을 때 시간이 더 적게 걸렸다. 등등

'''

def solution(s):
    candid = []
    if len(s) == 1: return 1
    for i in range(1, len(s)//2 + 1):
        lastToken, matchCount, result = '', 0, []
        for j in range(len(s)//i):
            token = s[j*i:(j+1)*i]

            # 주석도 달면 도움이 됩니다.
            if lastToken == token:
                matchCount += 1

                # print 문을 남기면 변수 추적 확인하는데 도움 될 수 있습니다~ ㅎㅎ
                # print(matchCount)
            else:
                matchCount = '' if matchCount < 2 else matchCount
                result.extend((str(matchCount), lastToken))
                lastToken = token
                matchCount = 1
        else:
            matchCount = '' if matchCount < 2 else matchCount
            result.extend((str(matchCount), lastToken))
            result.extend(s[(j+1)*i:])
        result = ''.join(result)
        candid.append(len(result))
    return min(candid)