from flask_restful import Resource
from get_data import get_exchange_rate,get_major_diff_between_buy_ask,get_max_min_avg
from process_data import process_exchange_rate,process_major_diff_between_buy_ask,process_max_min_avg
from constants import POSSIBLE_CURRENCY_CODES
from validators import check_currency_code,check_date,check_num_of_last_quot



#Setting the funcionalities for each endpoint
class Exchange(Resource):
    def get(self,currency_code,date):
        if not check_date(date): return "The date should be in format YYYY-MM-DD"
        if not check_currency_code(currency_code): return f"The currency code is invalid. The possible codes are: {POSSIBLE_CURRENCY_CODES}"
        data = get_exchange_rate(currency_code=currency_code,date=date)
        return process_exchange_rate(data)
    
class MaxMin(Resource):
    def get(self,currency_code,num_of_last_quot):
        if not check_num_of_last_quot(num_of_last_quot): return "The number of last quotations should be less than 255"
        if not check_currency_code(currency_code): return f"The currency code is invalid. The possible codes are: {POSSIBLE_CURRENCY_CODES}"
        data = get_max_min_avg(currency_code=currency_code,num_of_last_quot=num_of_last_quot)
        return process_max_min_avg(data)
    
class MajorDiff(Resource):
    def get(self,currency_code,num_of_last_quot):
        if not check_num_of_last_quot(num_of_last_quot): return "The number of last quotations should be less than 255"
        if not check_currency_code(currency_code): return f"The currency code is invalid. The possible codes are: {POSSIBLE_CURRENCY_CODES}"
        data = get_major_diff_between_buy_ask(currency_code=currency_code,num_of_last_quot=num_of_last_quot)
        return process_major_diff_between_buy_ask(data)
