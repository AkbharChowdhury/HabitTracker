import os
from datetime import date, timedelta, datetime

import requests
from constants import  Helper

pixela_endpoint = r'https://pixe.la/v1/users'
TOKEN = 'alskdnf2'
USERNAME = 'akbhard'
GRAPH_ID = 'graph1'


# https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
def main():
    user_params = {
        'token': str(TOKEN),
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': "yes"
    }
    # response = requests.post(url=pixela_endpoint, json=user_params)
    # print(response.text)
    graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

    graph_config = {
        'id': str(GRAPH_ID),
        'name': 'cycling graph'.title(),
        'unit': 'Km',
        'type': 'float',
        'color': 'shibafu'
    }
    headers = {
        'X-USER-TOKEN': str(TOKEN)
    }

    def post_data(url, json, headers_info):
        res = requests.post(url=url, json=json, headers=headers_info)
        print(res.text)

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

    pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
    # my_date = datetime.now().strftime('%Y%m%d')

    # date.today() - timedelta(3)
    my_date = date.today() - timedelta(3)

    print(my_date)

    pixel_data = {
        'date': Helper.format_time(my_date),
        'quantity': '15',
    }

    # post_data(url=pixel_creation_endpoint, json=pixel_data, headers_info=headers)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
#     https://pixe.la/v1/users/akbhard/graphs/graph1.html

#     pip install python-dotenv
