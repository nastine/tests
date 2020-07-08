import requests

API_KEY = "trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0"


def translate_it(text, from_lang, into_lang='ru', **kwargs):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': API_KEY,
        'text': text,
        'lang': "{}-{}".format(from_lang, into_lang)
    }

    response = requests.get(URL, params=params).json()
    return response


if __name__ == '__main__':
    print(translate_it('Hello', 'англ'))
