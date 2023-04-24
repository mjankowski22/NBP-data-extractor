import requests
from constants import SERVER_ADRESS

#Unit tests for the application

#Class for testing finding the average exchange rate feature
class TestExchangeRate:

    #Tests if data coming from the server is correct

    def test_correct_data(self):
        correct_average = 5.2768
        date= '2023-01-02'
        currency_code = 'GBP'
        response = requests.get(SERVER_ADRESS+f'exchanges/{currency_code}/{date}')
        data = response.json()
        assert data['average_exchange_rate'] == correct_average

    #Tests error handling

    def test_wrong_date(self):
        date = '2023-04-08' #weekend
        currency_code = 'GBP'
        response = requests.get(SERVER_ADRESS+f'exchanges/{currency_code}/{date}')
        assert response.status_code ==200
    
    def test_wrong_currency_code(self):
        date = '2023-01-02'
        currency_code = 'AAA' #invalid currency_code
        response = requests.get(SERVER_ADRESS+f'exchanges/{currency_code}/{date}')
        assert response.status_code ==200 

#Class for testing finding the max and min average exchange rate feature
class TestMaxMinAverage():

    #Tests if data coming from the server is correct
    def test_correct_data(self):
        correct_min = 2.8024
        correct_max = 3.1041
        correct_min_date = "2023-04-24"
        correct_max_date = "2023-02-13"
        currency_code = 'AUD'
        num_of_last_quot = 100
        response = requests.get(SERVER_ADRESS+f'max_min/{currency_code}/{num_of_last_quot}')
        data = response.json()
        assert data['max_min']['min']['value'] == correct_min
        assert data['max_min']['max']['value'] == correct_max
        assert data['max_min']['min']['date'] == correct_min_date
        assert data['max_min']['max']['date'] == correct_max_date

    #Tests error handling
    def test_wrong_currency_code(self):
        currency_code = 'AAA' #invalid currency code
        num_of_last_quot = 100
        response = requests.get(SERVER_ADRESS+f'max_min/{currency_code}/{num_of_last_quot}')
        assert response.status_code ==200

    def test_wrong_num_of_quots(self):
        currency_code='GBP'
        num_of_last_quot = 300 #>255
        response = requests.get(SERVER_ADRESS+f'max_min/{currency_code}/{num_of_last_quot}')
        assert response.status_code ==200

#Class for testing finding the major difference between buy and ask rate feature
class TestMajorDiff():

    #Tests if data coming from the server is correct
    def test_correct_data(self):
        correct_bid = 4.8172
        correct_ask = 4.9146
        correct_difference = 0.0974
        correct_date = '2022-10-11'
        currency_code = 'EUR'
        num_of_last_quot = 200
        response = requests.get(SERVER_ADRESS+f'major_diff/{currency_code}/{num_of_last_quot}')
        data = response.json()
        assert data['major_difference']['bid_value'] == correct_bid
        assert data['major_difference']['ask_value'] == correct_ask
        assert data['major_difference']['difference'] == correct_difference
        assert data['major_difference']['date'] == correct_date

    #Tests error handling
    def test_wrong_currency_code(self):
        currency_code = 'BBB' #invalid currency code
        num_of_last_quot = 100
        response = requests.get(SERVER_ADRESS+f'major_diff/{currency_code}/{num_of_last_quot}')
        assert response.status_code ==200

    def test_wrong_num_of_quots(self):
        currency_code='NOK'
        num_of_last_quot = 400 #>255
        response = requests.get(SERVER_ADRESS+f'major_diff/{currency_code}/{num_of_last_quot}')
        assert response.status_code ==200
