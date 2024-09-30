from http.client import responses

import configuration
import requests
import data



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_client_kit(kit_body):
    response = post_new_user(data.user_body)
    authorization = response.json()['authToken']
    header_kit = {
        'Authorization': f'Bearer {authorization}',
        'Content-Type': 'application/json'}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=header_kit
                          )





