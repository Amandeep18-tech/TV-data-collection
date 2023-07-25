
import requests
import header_values
import random
from time import sleep
from get_product_details import get_details,get_code
from make_csv_tv_data import make_header

params = {
    "currentPage": 0,
    "query": ":relevance",
    "fields": "FULL",
    "channel": "WEB",
    "channelCode": "400049",
}
make_header()
code_list=[]
while True:
    # URL='https://api.croma.com/searchservices/v1/category/999?currentPage=0&query=:relevance&fields=FULL&channel=WEB&channelCode=400049'

    base_url = "https://api.croma.com/searchservices/v1/category/999"
    
    random_header=random.choice(header_values.user_agents_list)
    
    headers = {'User-Agent': random_header,'Accept':header_values.accept,'Accept-Encoding':header_values.accept_encoding,'Connection':header_values.connection}
    res = requests.get(url = base_url, params=params, headers=headers)
    if res.status_code==200:
        sleep_time = random.uniform(8, 15)
        sleep(sleep_time)
        products_list=res.json()['products']
        # print(len(products_list))
        if len(products_list)==0:
            print(products_list)
            break
        for product in products_list:
            
            product_code=get_code(product)
            # print(product_code)
            # print(code_list)
            if product_code in code_list:
                continue
            get_details(product)
            code_list.append(product_code)
            
        params['currentPage']=params['currentPage']+1
        # print(params['currentPage'])
    
    


    