'''
* 유형
    heap

* 난이도
    *

* 풀이
    heap 자료구조를 사용한다.
    heap 추가, 최소값 삭제는 기본적인 heap 함수를 사용한다.
    최대값 삭제는 리스트에서 최대값을 삭제한다.

* 기타
    테스트케이스가 너무 빈약해서 지금 코드는 얼마나 비효율적인지 정확히 모르겠음.
    아마도 max 함수와 remove 함수를 계속 사용하니 최악의 경우에는 시간초과가 날 것.

    처음에 heap 을 2 개 만들어서 최소힙, 최대힙 2 개를 조작하는 방식이 더 효율일거라고 생각함.
    최대힙은 모든 원소에 마이너스를 붙여서 구성한다.
    그러면 max 함수나 remove 함수를 쓰지 않아도 되고 최악의 상황에서 효율적으로 돌아갈 것임.

'''

from heapq import heappop, heappush, heapify

def solution(operations):
    q = []
    for oper in operations:
        if oper[0] == 'I':
            heappush(q, int(oper[2:]))
        elif len(q) > 0 and oper[2] == '1':
            q.remove(max(q))
        elif len(q) > 0 and oper[2] == '-':
            heappop(q)
    if len(q) == 0:
        return [0, 0]
    else:
        return [max(q), min(q)]