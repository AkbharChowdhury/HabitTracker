import os
from datetime import date, timedelta
from dotenv import load_dotenv
import requests
from utils import Helper

# https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
def main():
    load_dotenv(override=False)
    pixela_endpoint = r'https://pixe.la/v1/users'
    TOKEN = os.getenv('TOKEN')
    # USERNAME = 'akbhard'
    USERNAME = os.getenv('USERNAME')
    GRAPH_ID = os.getenv("NAME")

    user_params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': "yes"
    }
    # response = requests.post(url=pixela_endpoint, json=user_params)
    # print(response.text)
    graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

    graph_config = {
        'id': GRAPH_ID,
        'name': 'cycling graph'.title(),
        'unit': 'Km',
        'type': 'float',
        'color': 'shibafu'
    }
    headers = {
        'X-USER-TOKEN': TOKEN
    }

    def post_data(url, json, headers_info):
        res = requests.post(url=url, json=json, headers=headers_info)
        print(res.text)

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

    pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
    # my_date = datetime.now().strftime('%Y%m%d')

    # date.today() - timedelta(3)
    my_date = date.today() - timedelta(12)

    print(my_date)
    amount = float(input('How many km?: '))

    pixel_data = {
        'date': Helper.format_time(my_date),
        'quantity': str(amount),
    }

    post_data(url=pixel_creation_endpoint, json=pixel_data, headers_info=headers)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
#     https://pixe.la/v1/users/akbhard/graphs/graph1.html
