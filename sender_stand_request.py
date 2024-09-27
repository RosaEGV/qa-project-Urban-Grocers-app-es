import configuration
import requests
import data



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())
authorization = response.json()['authToken']
print(authorization)

header_kit = {
        'Authorization': f'Bearer {authorization}',
        'Content-Type': 'application/json'
}
def post_new_client_kit(kit_body):
     return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=header_kit
    )
response = post_new_client_kit (data.kit_body)
print(response.status_code)
print(response.json())
