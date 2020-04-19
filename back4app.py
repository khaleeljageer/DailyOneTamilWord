import requests
import json
from local_settings import *


def update_status(objectId):
    url = "https://parseapi.back4app.com/classes/WordCorpus/"+objectId
    payload = {'status': True}
    header = {
<<<<<<< HEAD
        'X-Parse-Application-Id': X_PARSE_APPLICATION_ID,
        'X-Parse-REST-API-Key': X_PARSE_REST_API_KEY,
=======
        'X-Parse-Application-Id': 'application-Id',
        'X-Parse-REST-API-Key': 'rest-Api-Key',
>>>>>>> 73f2ab152ea72e14a3b43837e0f470c616a5128f
        'Content-Type': 'application/json'
    }

    response = requests.put(url, data=json.dumps(payload), headers=header)
    print(response.text)
    return response.status_code


class Back4App():
    def get_sentance(self):
        header = {
<<<<<<< HEAD
            'Content-Type': 'application/json',
            'X-Parse-Application-Id': X_PARSE_APPLICATION_ID,
            'X-Parse-REST-API-Key': X_PARSE_REST_API_KEY,
=======
            'content-type': 'application/json',
            'X-Parse-Application-Id': 'application-Id',
            'X-Parse-REST-API-Key': 'rest-Api-Key',
>>>>>>> 73f2ab152ea72e14a3b43837e0f470c616a5128f
        }
        url = "https://parseapi.back4app.com/classes/WordCorpus?where=%7B%22status%22%3Afalse%7D"
        data = requests.get(url, headers=header)
        json_response = data.json()

        results = json_response['results'][0]
        sentence = ('சொல் : %s,\nபொருள் : %s' %
                    (results['word'], results['meaning']))
        update_status(results['objectId'])
        tags = '\n#தினம் #ஒரு #தமிழ் #சொல்'
        return sentence+tags


if __name__ == "__main__":
    print("Try running daily_one_word.py first")
