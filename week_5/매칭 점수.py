'''

* 유형
    정규표현식, 구현

* 체감 난이도
    ****

* 풀이
    url, href, word 뽑아내는데 정규표현식을 잘 써야 한다.
    나머지는 해쉬 잘 만들면 되는데 정규표현식 잘못 쓰면 테스트케이스 예외가 난다.

    나같은 경우는 9, 10 번만 계속 틀렸음.
    url, href 뽑아내는 데 정규표현식 안쓰고 문자열 함수를 썼기 때문에 예외를 걸러낼 수 없었음.
    정규표현식을 안써도 불가능하지는 않았겠지만 gg

    정규표현식의 \S 는 공백을 제외한 모든 문자임.
'''

import re
def solution(word, pages):
    answer = 0

    # url - index 쌍
    page_map = {}

    # url - link 그래프. 링크 갯수.
    graph = {}

    # page 당 기본 점수
    basics = {}

    # page 당 link 점수
    link_scores = {}

    # page 들로 그래프 구성
    for i, page in enumerate(pages):
        links = []
        url = re.search('<meta property="og:url" content="(https://\S+)"', page).group(1)
        basics[url] = 0

        for link in re.findall('<a href="(https://\S+)"', page):
            links.append(link)

        for find in re.findall('[a-zA-Z]+', page):
            if find.upper() == word.upper():
                basics[url] += 1

        page_map[i] = url
        graph[url] = links

    # 링크 점수에 기본 점수 채우기
    link_scores = {b: 0 for b in basics}
    for page in basics:
        link_scores[page] += basics[page]

    # 각 page 들 링크 점수 계산 반영
    for page, links in graph.items():
        info = basics[page] / len(links) if links else 0

        for link in links:
            # print(page, link, info)
            try:
                link_scores[link] += info
            except:
                pass

    link_scores = sorted(link_scores.items(), key=lambda x: x[1], reverse=True)
    for i, page in page_map.items():
        if page == link_scores[0][0]:
            answer = i
            break

    return answer