import json
from pprint import pprint


def movie_info(movies, genres):
    ms = []
    for m in movies:
        infos = {
            'id': m.get('id'),
            'title': m.get('title'),
            'vote_average': m.get('vote_average'),
            'overview': m.get('overview')
        }

        n = []
        for i in m['genre_ids']:
            for j in genres:
                if j['id'] == i:
                    n.append(j['name'])

        infos['genres_names'] = n
        ms.append(infos)

    return ms
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
