from colorama import Fore

def print_stocks_table(rows: list, demo_symbols_list: list, symbols_list: list, color_indication_index: int, neutral_color: Fore): 
    maxLenght = []
    # finding lenghtiest words
    for row in rows:
        for item_index in range(len(row)):
            if item_index >= len(maxLenght):
                maxLenght.append(len(str(row[item_index])))
            elif len(row[item_index]) > maxLenght[item_index]:
                maxLenght[item_index] = len(row[item_index])
    # formatting word spacing 
    for row_index in range(len(rows)):
        for item_index in range(len(rows[row_index])):
            if len(rows[row_index][item_index]) < maxLenght[item_index]:
                new_item = rows[row_index][item_index]
                for i in range(maxLenght[item_index]-len(rows[row_index][item_index])):
                    new_item += " "
                rows[row_index][item_index] = new_item
    # combining lists to print out a message
    for row_index in range(len(rows)):
        print_message = ""
        color = neutral_color
        if row_index == 0:
            for item_index in range(len(rows[row_index])):
                print_message += demo_symbols_list[item_index]+rows[row_index][item_index]
            print(color+print_message)
        else:
            for item_index in range(len(rows[row_index])):
                print_message += symbols_list[item_index]+rows[row_index][item_index]
            if color_indication_index == -1:
                color = neutral_color
            elif float(rows[row_index][color_indication_index]) > 0: 
                color = Fore.GREEN
            elif float(rows[row_index][color_indication_index]) < 0:
                color = Fore.RED
            print(color+print_message)
    print()
