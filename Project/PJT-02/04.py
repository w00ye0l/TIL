import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3/'
    path = 'search/movie'
    params = {
        'api_key': 'afc82667845b09c1c37bd166abd0c812',
        'language': 'ko',
        'query': title
    }

    response = requests.get(
        BASE_URL + path, params=params).json().get('results', None)

    if not response:        # response가 비어있으면 None 리턴
        return None

    # '기생충'으로 검색했을 때 첫 번째 나오는 영화의 id 가져오기
    movie_id = response[0].get('id')

    path_2 = f'movie/{movie_id}/recommendations'        # 추천 영화를 가져오기 위한 경로
    response2 = requests.get(
        BASE_URL + path_2, params=params).json().get('results')         # 추천 영화들 정보 가져오기

    titles = []

    for i in response2:
        titles.append(i.get('title'))

    if titles == []:
        return []
    else:
        return titles
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
