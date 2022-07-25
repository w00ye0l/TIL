import requests
from pprint import pprint


def credits(title):
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

    path_2 = f'movie/{movie_id}/credits'        # 영화 크레딧를 가져오기 위한 경로
    response2 = requests.get(
        BASE_URL + path_2, params=params).json().get('results')         # 추천 영화들 정보 가져오기
    print(response2)

    dic = {}
    cast = []
    crew = []

    for i in response2:
        if cast['id'] < 10:
            cast.append(i.get('cast_id'))
    dic['cast'] = cast

    for i in response2:
        if crew['department'] == 'Directing':
            crew.append(i.get('department'))
    dic['crew'] = crew

    if dic == {}:
        return []
    else:
        return dic
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
