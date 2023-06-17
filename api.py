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
        stocks_json["investments"][i]["procentage_shift"] = str(calculate_stocks_shift_procentage(stocks_json["investments"][i]["profit"], stocks_json["investments"][i]["buy_price"], stocks_json["investments"][i]["last_known_price"]))
        combined_profit += profit
    lost_to_tax = round(float(combined_profit)*float(tax), 2)
    stocks_json["combined_profit_tax_free"] = round(combined_profit, 2)
    stocks_json["combined_profit"] = round(combined_profit-lost_to_tax, 2)
    stocks_json["lost_to_tax"] = round(float(combined_profit)*float(tax), 2)
    portfolio_shift = [0, 0] 
    for i in stocks_json["investments"]:
        portfolio_shift[0] += i["starting_sum"]
    portfolio_shift[1] = round(float(portfolio_shift[0] + stocks_json["combined_profit"]), 2)
    stocks_json["portfolio_shift"] = str(portfolio_shift[0])+" -> "+str(portfolio_shift[1])
    stocks_json["portfolio_procentage_shift"] = calculate_stocks_shift_procentage(stocks_json["combined_profit"], portfolio_shift[0], portfolio_shift[1])
    write_local_stocks_json(stocks_json)
    return stocks_json

def get_current_price(ticker: str):
    headers = {"Content-Type": "application/json; charset=utf-8","User-Agent" : "PostmanRuntime/7.29.2"}
    api_response = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/'+ticker, headers=headers)._content
    current_price = json.loads(api_response)["chart"]["result"][0]["meta"]["regularMarketPrice"]
    return round(current_price, 2)