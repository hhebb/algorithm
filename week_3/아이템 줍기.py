''''
* 유형
    BFS, 도형

* 체감 난이도
    ****

* 풀이
    1. 직사각형들이 이루는 큰 polygon 의 테두리를 딴다.
        1.1. 크기가 50x2 만큼의 board 를 생성한다.
        1.2. 각 사각형을 가로 세로 2 배 늘려서 내부를 모두 1 로 채운다.
        1.3. 각 사각형을 가로 세로 2 배 늘리고 테두리를 제외한 곳을 모두 0 으로 채운다.
    2. 시작점으로부터 아이템이 있는 곳 까지 최단거리를 구한다.
        2.1. 최단거리를 기록할 배열 dists 를 생성한다.
        2.2. 캐릭터의 위치로부터 BFS 를 돌린다.
        2.2. 이동방향은 시계 방향, 반시계 방향 2 개 뿐이므로 둘 중 작은 거리값을 선택
        2.3. 원래 사이즈대로 하기 위해 2 를 나눈다.


    ----------------------------

    1. 도형 겹침
    처음에 edge 끼리 교점을 구하고 그 교점을 새로 합쳐진 도형의 point 로 만드는 등 방법을 생각했지만 너무 어려웠음.
    일반적으로 polygon 집합 연산하듯이 그냥 내부를 1 로 채우면 간편한 작업이었음.

    2. 테두리 따기
    원래 도형이
        x1 < x < x2,
        y1 < y < y2, 일 때
    테두리(perimeter) 는
        x1+1 < x < x2-1,
        y1+1 < y < y2-1, 을 제거한 활용한다.

    original   inside

    ******
    ******     *****
    ******     *****
    ******

    단, 이 문제에선 edge 가 겹치는 곳이 없다고 했으니 그 부분을 별도로 처리하지 않아도 되었지만
    만약 edge 가 겹치는것이 허용된다면, 그 부분은 별도로 0 으로 처리해줘야 정상적으로 테두리를 딸 수 있음.


'''


dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX, characterY, itemX, itemY = [coord * 2 for coord in [characterX, characterY, itemX, itemY]]
    board = [[0] * 101 for r in range(101)]

    # polygon 채우기
    for r1, c1, r2, c2 in rectangle:
        for r in range(r1 * 2, r2 * 2 + 1):
            for c in range(c1 * 2, c2 * 2 + 1):
                board[r][c] = 1

    # perimeter 따기
    # 만약 edge 가 중복이 되면 이 알고리즘 작동 안함.
    for r1, c1, r2, c2 in rectangle:
        for r in range(r1 * 2 + 1, r2 * 2):
            for c in range(c1 * 2 + 1, c2 * 2):
                board[r][c] = 0

    # BFS
    q = [(characterX, characterY)]
    visited = [[False] * 101 for r in range(101)]
    dists = [[0] * 101 for r in range(101)]
    candid = []

    while len(q) > 0:
        r, c = q.pop()

        for d in range(4):
            nextR, nextC = r + dr[d], c + dc[d]

            if nextR == itemX and nextC == itemY:
                candid.append(dists[r][c])
                break

            if not (0 <= nextR < 101 and 0 <= nextC < 101):
                continue

            if board[nextR][nextC] and not visited[nextR][nextC]:
                visited[nextR][nextC] = True
                dists[nextR][nextC] = dists[r][c] + 1
                q.append((nextR, nextC))

    return (min(candid) + 1) // 2