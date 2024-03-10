import random




#global_variables
MAX__LINES = 3
MIN__LINES = 1
MAX__BET = 1000
ROWS = 3
COLUMNS = 3
symbol_counts = {"A":2,"B":4,"C":6,"D":8}  #the symbols which will appear on slot machine



def slot_machine_random_symbols(rows,columns,symbols):
    whole_symbols= [symbol for symbol,symbol_count in symbols.items()  for i in range(symbol_count)] #used list comprehension to store the symbols depends upon their frequency
    slot_machine = []
    all_symbols = whole_symbols[:] #make the copy of the list so that the real list won't be changed
    for i in range(rows):
        row = []
        all_symbols = whole_symbols[:] #make the copy of the list so that the real list won't be changed we put inside the for loop so that in every iteration of outer loop the same list will be copied.
        for j in range(columns):
            value = random.choice(all_symbols)
            row.append(value)
            all_symbols.remove(value)
        slot_machine.append(row)
    return slot_machine    



def print_slot_machine_column(fx):  #to change the rows into column because we want data in the form of columns not in rows.
    for i in range(len(fx)):
        for j in range(len(fx[0])):
           print(fx[j][i],end=" | ") #transpose the matrix row into column
        print(end="\n")
        
    
        


def deposit_cash():     #deposit the cash 
    while True:
        print(f"The max amount for bet is ${MAX__BET} \n")
        amount = input("Enter the amount which you want to deposit:$ ")
        if amount.isdigit():   
            amount = int(amount)
            if 0<amount<=1000:
                break
            else:
                print(f"Enter the value greater than zero or less than {MAX__BET}.")
        else:
            print("Enter a valid number.")
            
    return amount
            

def bet_lines():  #decide how many ine you should add on bat
    while True:
        lines = input(f"Enter the lines which you want to bet on {MIN__LINES}-{MAX__LINES}: ")
        if lines.isdigit():
            lines = int(lines)
            if  1<=lines<=3:                
                break
            else:
                print(f"Enter the value in between {MIN__LINES} and {MAX__LINES} inclusively. ")
        else:
            print("Enter a valid number.")
            
    return lines       
            
def bet_amount():
    while True:
        bet_amount = input(f"Enter the amount which you want to bet on each line:$ ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount>0:
                break
            else:
                print(f"Enter the amount greater than zero.")
        else:
            print("Enter a valid number.")
            
    return bet_amount

def main():  #defining main function.
    deposit_amount = deposit_cash()
    bet_line = bet_lines()
    
    while True:
        bet_amount_line = bet_amount()
        if bet_amount_line*bet_line<=deposit_amount:
            break
        else:
            print(f"You entered the value which is greater than the deposit amount your total deposit is {int(deposit_amount)} so you can max enter the amount of ${int(deposit_amount/bet_line)}")
    print(f"You bet on each line ${bet_amount_line} and your total amount for bet is ${bet_amount_line*bet_line}")
    rows = slot_machine_random_symbols(ROWS,COLUMNS,symbol_counts)
    print_slot_machine_column(rows)
main()
    