from table_creator import print_stocks_table
from colorama import Fore

def present_initial():
    print(Fore.CYAN+
    "            __              __        \n"+
    "      _____/ /_____  ____  / /_______ \n"+
    "     / ___/ __/ __ \/ __ \/ //_/ ___/ \n"+
    "    (__  ) /_/ /_/ / / / / ,< (__  )  \n"+
    "   /____/\__/\____/_/ /_/_/|_/____/   \n"
    )
    print("\x1B[3m   Stonks calculator 3000 1.0v \x1B[3m")

def present_options():
    print("\033[0m")
    print(
        "[1] Add investment\n"+
        "[2] Remove investment\n"+
        "[3] Change tax procentage\n"+
        "[4] Synch investments\n"+
        "[5] Local stored investments data\n"+
        "[e] Exit\n")

def present_main_table(stocks_json):
    # INDIVIDUAL
    print("\033[0m")
    rows = [["Stock label", "Profit", "Investment shift", "Stock price shift"]]
    for i in stocks_json["investments"]:
        rows.append([str(i["ticker"]), str(i["profit"]), str(i["starting_sum"])+" -> "+str(i["current_sum"]), str(i["buy_price"])+" -> "+str(i["last_known_price"])])
    demo_symbols_list = ["   ", "   |   ", " / ", "   |   "]
    symbols_list = [" ○ ", "   •   ", " / ", "   •   "]
    print_stocks_table(rows, demo_symbols_list, symbols_list, 1, Fore.LIGHTBLACK_EX)
    # OVERALL
    portfolio_shift = [0, 0] 
    for i in stocks_json["investments"]:
        portfolio_shift[0] += i["starting_sum"]
    portfolio_shift[1] = portfolio_shift[0] + stocks_json["combined_profit"]
    rows = [["Overall profit", "Tax free", "Lost to tax", "Portfolio shift"], [str(stocks_json["combined_profit"]), str(stocks_json["combined_profit_tax_free"]), str(stocks_json["lost_to_tax"]), str(portfolio_shift[0])+" -> "+str(portfolio_shift[1])]]
    demo_symbols_list = ["   ", " / ", "   |   ", "   |   "]
    symbols_list = [" ○ ", " / ", "   •   ", "   •   "]
    print_stocks_table(rows, demo_symbols_list, symbols_list, 0, Fore.LIGHTBLACK_EX)

def present_remove_investment_list(stocks_json):
    rows = [["Label", "Starting sum", "Timestamp"]]
    for index in range(len(stocks_json["investments"])):
        rows.append(["["+str(index+1)+"] "+str(stocks_json["investments"][index]["ticker"]), str(stocks_json["investments"][index]["starting_sum"]), str(stocks_json["investments"][index]["investment_timestamp"])])
    demo_symbols_list = ["", "   |   ", "   |   "]
    symbols_list = ["", "   •   ", "   •   "]
    print_stocks_table(rows, demo_symbols_list, symbols_list, -1, Fore.WHITE)

def present_empty():
    print("\033[0m")
    print(Fore.LIGHTBLACK_EX+"No investments to display")

def present_empty_on_remove():
    print("\033[0m")
    print(Fore.LIGHTBLACK_EX+"No investments to remove")