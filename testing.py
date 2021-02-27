# import requests
# r = requests.get('https://scrambled-api.mysportsfeeds.com/v2.1/pull/mlb/2021-regular/games/20210627-SEA-CWS/boxscore.json', auth=('8e039d46-b4d6-44f2-b3b9-b9ba42', 'MYSPORTSFEEDS'))
# print(r.json())
import json

def get_boxscore() -> tuple:
    with open('ex_boxscore.json') as f:
        data = json.load(f)

    ar = data['scoring']['awayScoreTotal']
    ah = data['scoring']['awayHitsTotal']
    ae = data['scoring']['awayErrorsTotal']

    hr = data['scoring']['homeScoreTotal']
    hh = data['scoring']['homeHitsTotal']
    he = data['scoring']['homeErrorsTotal']

    away = '{0:<2d} {1:<2d} {2:<2d}'.format(ar, ah, ae)
    home = '{0:<2d} {1:<2d} {2:<2d}'.format(hr, hh, he)

    return away, home


if __name__ == '__main__':
    boxscore = get_boxscore()
    print('{:2s} {:2s} {:2s}'.format('R', 'H', 'E'))
    print(boxscore[0])
    print(boxscore[1])