import requests
import json


def update_status(objectId):
    url = "https://parseapi.back4app.com/classes/WordCorpus/"+objectId
    payload = {'status': True}
    header = {
        'X-Parse-Application-Id': 'application-Id',
        'X-Parse-REST-API-Key': 'rest-Api-Key',
        'Content-Type': 'application/json'
    }

    response = requests.put(url, data=json.dumps(payload), headers=header)
    print(response.text)
    return response.status_code

class Back4App():
    def __init__(self):
        self.beginnings = []
        self.freq = {}

    def get_sentance(self):
        header = {
            'content-type': 'application/json',
            'X-Parse-Application-Id': 'application-Id',
            'X-Parse-REST-API-Key': 'rest-Api-Key',
        }
        url = "https://parseapi.back4app.com/classes/WordCorpus?where=%7B%22status%22%3Afalse%7D"
        data = requests.get(url, headers=header)
        json_response = data.json()

        results = json_response['results'][0]
        sentence = ('சொல் : %s,\nபொருள் : %s' %
                    (results['word'], results['meaning']))
        update_status(results['objectId'])
        return sentence


if __name__ == "__main__":
    print("Try running daily_one_word.py first")
