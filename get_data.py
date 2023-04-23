import requests
from constants import ENDPOINT

#Function to make the request to the server
def make_request(url:str) -> dict:
    """Makes request to the NBP API"""
    headers={
        'format':'json'
    }
    try:
        response = requests.get(url=url,headers=headers)
        response.raise_for_status()
        data= response.json()
        return data
    except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred: " + repr(errh)
    except requests.exceptions.ConnectionError as errc:
            return "An Error Connecting to the API occurred: " + repr(errc)
    except requests.exceptions.Timeout as errt:
            return "A Timeout Error occurred: " + repr(errt)
    except Exception as err:
            return "An Unknown Error occurred:  " + repr(err)
    

#Functions to get the correct endpoint and execute request

def get_exchange_rate(currency_code:str,date:str):
    """Configuring endpoint for getting the average exchange rate and making a request"""
    url = ENDPOINT+f'a/{currency_code}/{date}'
    return make_request(url)

def get_max_min_avg(currency_code:str,num_of_last_quot:int):
    """Configuring endpoint for getting the minimum and maximum average exchange rate in the last quotations and making a request"""
    url = ENDPOINT +f'a/{currency_code}/last/{num_of_last_quot}'
    return make_request(url)

    
def get_major_diff_between_buy_ask(currency_code:str,num_of_last_quot:int):
    """Configuring endpoint for getting the major difference of ask and sell rate and making a request"""
    url = ENDPOINT +f'c/{currency_code}/last/{num_of_last_quot}'
    return make_request(url)
