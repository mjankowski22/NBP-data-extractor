from pandas import DataFrame


#Function to process the data got from the NBP API

def check_data(data) -> bool:
    """Checking if there was an error in NBP API response"""
    return False if type(data) == str else True
    

def process_exchange_rate(data:dict)->dict:
    """Process the data got from the server to get average exchange rate"""
    if not check_data(data): 
        return data
    answer = {
        'currency':data['currency'],
        'code':data['code'],
        'date':data['rates'][0]['effectiveDate'],
        'average_exchange_rate':data['rates'][0]['mid']
    }
    return answer

def process_max_min_avg(data:dict)->dict:
    """Process the data got from the server to get max and min average exchange rate"""
    if not check_data(data): 
        return data
    framed_data = DataFrame(data['rates'])
    max_id = framed_data['mid'].idxmax()
    min_id = framed_data['mid'].idxmin()
    answer={
        'currency':data['currency'],
        'code':data['code'],
        'max_min':{
            'min':{
                'value':framed_data.at[min_id,'mid'],
                'date':framed_data.at[min_id,'effectiveDate']
            },
            'max':{
                'value':framed_data.at[max_id,'mid'],
                'date':framed_data.at[max_id,'effectiveDate']
            }
        }
    }
    return answer

def process_major_diff_between_buy_ask(data:dict)->dict:
    """Process the data got from the server to get major difference between bid and ask rate"""
    if not check_data(data): 
            return data
    framed_data = DataFrame(data['rates'])
    framed_data['difference'] = abs(framed_data['ask']-framed_data['bid'])
    max_id = framed_data['difference'].idxmax()
    answer = {
        'currency':data['currency'],
        'code':data['code'],
        'major_difference':{
            'date':framed_data.at[max_id,'effectiveDate'],
            'bid_value': framed_data.at[max_id,'bid'],
            'ask_value': framed_data.at[max_id,'ask'],
            'difference': round(framed_data.at[max_id,'difference'],4)}
    
    }
    return answer
    