import requests
import json
from bs4 import BeautifulSoup
from util import *

def synch_data(stocks_json):
    tax = stocks_json["tax_procentage"]
    combined_profit = 0
    for i in range(len(stocks_json["investments"])):
        current_price = get_current_price(stocks_json["investments"][i]["ticker"])
        if stocks_json["investments"][i]["buy_price"] == 0:
            stocks_json["investments"][i]["buy_price"] = current_price
        stocks_json["investments"][i]["last_known_price"] = float(current_price)
        profit =  calculate_profit(
            buy_price = float(stocks_json["investments"][i]["buy_price"]), 
            current_price = float(current_price), 
            starting_sum = float(stocks_json["investments"][i]["starting_sum"]))
        stocks_json["investments"][i]["profit"] = profit
        stocks_json["investments"][i]["current_sum"] = round(stocks_json["investments"][i]["starting_sum"]+profit, 2)
        combined_profit += profit
    lost_to_tax = round(float(combined_profit)*float(tax), 2)
    stocks_json["combined_profit_tax_free"] = round(combined_profit, 2)
    stocks_json["combined_profit"] = round(combined_profit-lost_to_tax, 2)
    stocks_json["lost_to_tax"] = round(float(combined_profit)*float(tax), 2)
    stocks_json_file_writable = open("stocks.json", "w")
    stocks_json_file_writable.write(str(stocks_json))
    stocks_json_file_writable.close()
    write_local_stocks_json(stocks_json)
    return stocks_json

def get_current_price(ticker: str):
    headers = {"Content-Type": "application/json; charset=utf-8","User-Agent" : "PostmanRuntime/7.29.2"}
    api_response = requests.get('https://finance.yahoo.com/quote/'+ticker+'?p='+ticker+'&.tsrc=fin-srch',headers=headers)
    soup = BeautifulSoup(api_response.content, "html.parser")
    current_price = soup.find(attrs={"data-symbol" : ticker}).text
    return current_price