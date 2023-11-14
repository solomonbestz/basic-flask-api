import requests
import json


def dump_data(data: json)-> None:
    with open('data.json', 'w') as file:
        file.write(json.dumps(data, indent=4))


if __name__=='__main__':
    response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

    for data in response.json()['items']:
       if data['answer_count'] < 5:
           dump_data(data)
    
