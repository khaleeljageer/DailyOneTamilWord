import requests
import json


def update_status(objectId):
    url = "https://parseapi.back4app.com/classes/WordCorpus/"+objectId
    payload = {'status': True}
    header = {
        'X-Parse-Application-Id': 'uegNg5eWDj8UY19XkhzeQMUWcvkNqza17TaLRq22',
        'X-Parse-REST-API-Key': 'qyIGngnRAqRvf8oXf9r2MhhaN1iDzcr68V5M91oo',
        'Content-Type': 'application/json'
    }

    response = requests.put(url, data=json.dumps(payload), headers=header)
    print(response.text)
    return response.status_code


class Back4App():
    def get_sentance(self):
        header = {
            'content-type': 'application/json',
            'X-Parse-Application-Id': 'uegNg5eWDj8UY19XkhzeQMUWcvkNqza17TaLRq22',
            'X-Parse-REST-API-Key': 'qyIGngnRAqRvf8oXf9r2MhhaN1iDzcr68V5M91oo'
        }
        url = "https://parseapi.back4app.com/classes/WordCorpus?where=%7B%22status%22%3Afalse%7D"
        data = requests.get(url, headers=header)
        json_response = data.json()

        results = json_response['results'][0]
        sentence = ('சொல் : %s,\nபொருள் : %s' %
                    (results['word'], results['meaning']))
        update_status(results['objectId'])
        tags = '#தினம் #ஒரு #தமிழ் #சொல்'
        return sentence+tags


if __name__ == "__main__":
    print("Try running daily_one_word.py first")
