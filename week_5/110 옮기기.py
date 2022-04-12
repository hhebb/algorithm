'''
* 유형
    배열 다루기, 구현

* 체감 난이도
    ****

* 풀이
    110 은 111, 1111, 1111.... 보다 작음을 이용한다.

    1. 원래 문자열에서 110 을 모두 제거하고 그 갯수를 센다.
    2. 남은 문자열을 역순으로 돌며 연속된 1 갯수를 센다.
    3. 남은 문자열[:len(남은 문자열) -연속된 1 갯수] + 110 갯수만큼 110 + 연속된 1 갯수만큼 1
    
    level 2 에 비슷한 유형의 문제들이 3~4 개 정도 있었던거 같았는데 뭔가 더 까다로웠던 거 같음.
    머리가 아파서 답안을 봐버렸다.. ㅠ
    코드로 보면 몇 줄 안되는데 그 아이디어 뽑아내는게 쉽지가 않다.

'''


def solution(s):
    answer = []

    for string in s:
        stack = []
        count_110 = 0
        for str in string:
            # 110이 나온 경우
            if (len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and str == '0'):
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str)

        # 110을 모두 제거했으므로 남은 문자열에서 연속된 1이 존재하는 곳은 한 곳밖에 없다.
        count_1 = 0
        for s in stack[::-1]:
            if s == '0':
                break
            else:
                count_1 += 1
        answer.append(''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)
    return answer