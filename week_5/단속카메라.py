'''
* 유형
    그리디

* 체감 난이도
    **

* 풀이
    1. routes 를 도착점 기준으로 정렬한다.
    2. 첫 route 의 도착점에 카메라를 설치하고, 다음 각 route 부터 출발점과 도착점 (끝점 포함)이 카메라 위치를 포함하는 지 검사.
        2.1. 포함한다면 pop 하면서 계속 진행
        2.2. 포함하지 않는다면 해당 route 도착점에 카메라를 추가로 설치하고 pop

'''


def solution(routes):
    routes = sorted(routes, key=lambda x:x[1])
    pos = routes.pop(0)[1]
    count = 1
    while len(routes) > 0:
        start, end = routes.pop(0)
        if not(start <= pos <= end):
            count += 1
            pos = end
    return count