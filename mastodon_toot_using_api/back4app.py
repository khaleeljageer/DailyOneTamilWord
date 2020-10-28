import requests
import json
from secret_keys import *


def get_headers():
    return {
        'X-Parse-Application-Id': X_PARSE_APPLICATION_ID,
        'X-Parse-REST-API-Key': X_PARSE_REST_API_KEY,
        'Content-Type': 'application/json'
    }


def update_status(objectId):
    url = "https://parseapi.back4app.com/classes/WordCorpus/"+objectId
    payload = {'status': True}
    header = get_headers()
    response = requests.put(url, data=json.dumps(payload), headers=header)
    print(response.text)
    return response.status_code

class Back4App():
    def get_sentance(self):
        header = get_headers()
        url = "https://parseapi.back4app.com/classes/WordCorpus?where=%7B%22status%22%3Afalse%7D"
        data = requests.get(url, headers=header)
        print(data)
        json_response = data.json()
        print(json_response)
        results = json_response['results'][0]
        #for i in results['meaning']:
            #print(i)

        sentence = ("சொல் : %s \n பொருள் : %s" %
                    (results['word'], results['meaning']))
        update_status(results['objectId'])
        tags = "\n#தினமொரு #தமிழ்_சொல்"
        return sentence+tags


if __name__ == "__main__":
    print("Try running daily_one_word.py first")