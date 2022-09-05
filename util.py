import json
from os.path import expanduser

def calculate_profit(buy_price: float, current_price: float, starting_sum: float):
    return round((current_price/buy_price)*starting_sum-starting_sum, 2)

def read_local_stocks_json():
    stocks_json_file_readable = open(str(expanduser("~"))+"/stonks-cli/stocks.json", "r")
    stocks_json = json.load(stocks_json_file_readable)
    return stocks_json

def write_local_stocks_json(stocks_json):
    with open(str(expanduser("~"))+'/stonks-cli/stocks.json', 'w', encoding='utf-8') as file:
        json.dump(stocks_json, file, ensure_ascii=False, indent=4)

def check_if_empty(stocks_json):
    if len(stocks_json["investments"]) == 0:
        return True
    else:
        return False

def calculate_stocks_shift_procentage(profit: float, buy_price: float, last_known_price: float):
    stocks_procentage = "▲ "
    if profit < 0:
        stocks_procentage = "▼ "
    return stocks_procentage+str(round((100*last_known_price)/float(buy_price)-100, 2))+" %"