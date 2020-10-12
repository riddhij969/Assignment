import requests
import sys, json

def get_token():
    #Get auth token
    url = "http://127.0.0.1:8000/api/auth/"
    response = requests.post(url, data= {'Username': 'Riddhi', 'Password': 'Rj@123456'})
    return response.json()

def get_data():

    url = "http://127.0.0.1:8000/api/products_list/"
    headers = {'Authorization': f'Token{get_token()}'}
    response = requests.get(url, headers = headers)
    prod_data = response.json()
    for i in prod_data:
        print(i)

get_data()