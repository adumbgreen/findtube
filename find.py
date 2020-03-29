import sys
import itertools
import requests

API_KEY = "null"


def url_for(video_id):
    return "https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=id".format(API_KEY, video_id)


def main(query_id):
    good = []
    case_combos = list(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in query_id))))
    print("{} combos".format(len(case_combos)))
    for random_id in case_combos:
        combo_url = url_for(random_id)
        response = requests.get(combo_url).json()
        if response.get('items'):
            good.append(combo_url.format(combo_url))
            print('found good link: https://youtube.com/watch?v={}'.format(random_id))
        else:
            print('bad id: {}'.format(random_id))

    print("\n".join(good))


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Usage: find.py video_id')
        exit()

    main(sys.argv[1])
