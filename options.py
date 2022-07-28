from api import *
from presentation import *
import os

def option_add():
    os.system('clear')
    present_initial()
    print("\033[0m")
    label = input("Investment ticker: ")
    timestamp = input("Timestamp: ")
    try:
        starting_sum = float(input("Starting sum: "))
    except:
        print(Fore.LIGHTBLACK_EX+"Invalid starting sum")
        return
    try:
        stocks_json = read_local_stocks_json()
        stocks_json["investments"].append(
            {
                "ticker": label,
                "starting_sum": starting_sum,
                "current_sum": 0,
                "buy_price": get_current_price(label),
                "last_known_price": 0,
                "profit": 0,
                "investment_timestamp": timestamp
            }
        )
        write_local_stocks_json(stocks_json)
        print(Fore.LIGHTBLACK_EX+"Investment added")
    except:
        print(Fore.LIGHTBLACK_EX+"Invalid investment ticker")
        return

def option_remove():
    os.system('clear')
    present_initial()
    stocks_json = read_local_stocks_json()
    print("\033[0m")
    present_remove_investment_list(stocks_json)
    print()
    try:
        user_input = int(input("Select which investment to remove: "))
        if user_input <= len(stocks_json["investments"]):
            stocks_json["investments"].pop(user_input-1)
            write_local_stocks_json(stocks_json)
    except:
        print(Fore.LIGHTBLACK_EX+"Unknown input")

def option_tax():
    os.system('clear')
    present_initial()
    stocks_json = read_local_stocks_json()
    print("\033[0m")
    try:
        user_iput = float(input("Enter tax procentage [0.01-0.99)]: "))
        if(0.01 <= user_iput <= 0.99):
            stocks_json["tax_procentage"] = user_iput
            write_local_stocks_json(stocks_json)
    except:
        print(Fore.LIGHTBLACK_EX+"Unknown input")

def option_stonks_synch():
    os.system('clear')
    present_initial()
    stocks_json = synch_data()
    present_main_table(stocks_json)

def option_stonks_local():
    os.system('clear')
    present_initial()
    stocks_json = read_local_stocks_json()
    present_main_table(stocks_json)

def option_exit():
    os.system('clear')