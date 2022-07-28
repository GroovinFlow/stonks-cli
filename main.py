
from presentation import *
from options import *

present_initial()

def loop():
    present_options()
    user_input = str(input())
    if(user_input == "1"):
        option_add()
        loop()
    elif(user_input == "2"):
        option_remove()
        loop()
    elif(user_input == "3"):
        option_tax()
        loop()
    elif(user_input == "4"):
        option_stonks_synch()
        loop()
    elif(user_input == "5"):
        option_stonks_local()
        loop()
    else:
        option_exit()

loop()