import json

def calculate_profit(buy_price: float, current_price: float, starting_sum: float):
    return round((current_price/buy_price)*starting_sum-starting_sum, 2)

def read_local_stocks_json():
    stocks_json_file_readable = open("/home/azuolas/Documents/vscode/stonks-cli/stocks.json", "r")
    stocks_json = json.load(stocks_json_file_readable)
    return stocks_json

def write_local_stocks_json(stocks_json):
    with open('/home/azuolas/Documents/vscode/stonks-cli/stocks.json', 'w', encoding='utf-8') as file:
        json.dump(stocks_json, file, ensure_ascii=False, indent=4)

