'''
* 유형
    DFS, 배열

* 체감 난이도
    ****+

* 풀이
    1. board 에서 빈 칸 덩어리들을 뽑아낸다. (blanks)
    2. table 에서 도형들을 뽑아낸다. (blocks)
    3. table 의 도형들을 돌려가면서 blanks 에 맞춰본다.
        3.1. blank 의 시작점을 최대한 원점으로 당긴다.
        3.2. block 도 시작점을 최대한 원점으로 당긴다.
        3.3. block 을 포함하는 직사각형을 따로 만든다. (box)
        3.4. box 를 4 방향으로 회전시키며 다시 block 의 좌표를 뽑아낸다.
        3.5. 현재 blank 와 현재 block 이 사용되지 않았고, block 좌표와 blank 좌표가 같은지 비교
        3.6. 같다면 block 과 blank 의 인덱스를 기록하고 answer 에 block 길이를 더해주고, 다음 blank 로 넘어간다.


    ----------------------------

    지금까지 본 matrix 다루는 문제 중 가장 복잡한 듯. 저저번주의 열쇠와 자물쇠보다 조금 더 어려운 듯.

    근데 아마 더 간단하게 풀 수 있을 것 같음.
    table 의 값을 반전시키면 재귀 함수 중복되는거 처리할 수 있을 듯.

    주석 필요.

'''


dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


def solution(game_board, table):
    answer = 0

    # for board
    def recur(r, c):
        if game_board[r][c]:
            return

        if len(poly) == 0 and not visited[r][c]:
            poly.append((r, c))
            visited[r][c] = True

        for d in range(4):
            nextR, nextC = r + dr[d], c + dc[d]
            if 0 <= nextR < len(game_board) and 0 <= nextC < len(game_board) and game_board[nextR][nextC] == 0:
                if not visited[nextR][nextC]:
                    visited[nextR][nextC] = True
                    poly.append((nextR, nextC))
                    recur(nextR, nextC)

    def recur2(r, c):
        if not table[r][c]:
            return

        if len(poly) == 0 and not visited[r][c]:
            poly.append((r, c))
            visited[r][c] = True

        for d in range(4):
            nextR, nextC = r + dr[d], c + dc[d]
            if 0 <= nextR < len(table) and 0 <= nextC < len(table) and table[nextR][nextC]:
                if not visited[nextR][nextC]:
                    visited[nextR][nextC] = True
                    poly.append((nextR, nextC))
                    recur2(nextR, nextC)

    #
    blanks = []
    blocks = []

    visited = [[False] * len(game_board) for r in range(len(game_board))]
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            poly = []
            recur(row, col)
            if len(poly) > 0:
                blanks.append(poly)

    visited = [[False] * len(table) for r in range(len(table))]
    for row in range(len(table)):
        for col in range(len(table)):
            poly = []
            recur2(row, col)
            if len(poly) > 0:
                blocks.append(poly)

    fill_idx1 = []
    fill_idx2 = []
    for bi1, blank in enumerate(blanks):
        min_r = min(blank)[0]
        min_c = min(blank, key=lambda x: x[1])[1]
        blank = sorted([(br - min_r, bc - min_c) for br, bc in blank])

        for bi2, block in enumerate(blocks):
            if len(blank) == len(block) and bi1 not in fill_idx1 and bi2 not in fill_idx2:
                min_r = min(block)[0]
                min_c = min(block, key=lambda x: x[1])[1]
                block = sorted([(br - min_r, bc - min_c) for br, bc in block])
                box = [[0] * (max(block, key=lambda x: x[1])[1] + 1) for rr in range(max(block)[0] + 1)]
                for r, c in block:
                    box[r][c] = 1

                # 뗴어낸 box 를 회전시킴.
                for i in range(4):
                    box = list(zip(*box))[::-1]
                    block = []
                    for r in range(len(box)):
                        for c in range(len(box[0])):
                            if box[r][c] == 1:
                                block.append((r, c))

                    if blank == block:
                        answer += len(blank)
                        fill_idx1.append(bi1)
                        fill_idx2.append(bi2)
                        break
    return answer