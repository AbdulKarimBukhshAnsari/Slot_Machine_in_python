import random



#global_variables
MAX__LINES = 3
MIN__LINES = 1

def deposit_cash():
    while True:
        amount = input("Enter the amount which you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Enter the value greater than zero.")
        else:
            print("Enter a valid number.")
    return amount
            

def bet_lines():
    while True:
        lines = input(f"Enter the lines which you want to bet on {MIN__LINES}-{MAX__LINES}: ")
        if lines.isdigit():
            lines = int(lines)
            if  1<=lines<=3:                
                break
            else:
                print("Enter the value in between 1 and 3 inclusively. ")
        else:
            print("Enter a valid number.")
            
            
deposit_cash()
bet_lines()