import random




#global_variables
MAX__LINES = 3
MIN__LINES = 1
MAX__BET = 1000
ROWS = 3
COLUMNS = 3
symbol_counts = {"A":3,"B":5,"C":7,"D":9}  #the symbols which will appear on slot machine
symbol_values = {"A":9,"B":7,"C":5,"D":3}  #the values of each symbol. 



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

def column(fx):
    columns = []
    for k in range(len(fx)):
        temp =[]
        for l in range(len(fx[0])):
            temp.append(fx[l][k])
        columns.append(temp)
    return columns

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
            

def bet_lines():  #decide how many lline you should add on bat
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


def winning(slots,lines,values,bet_value):
    winner_lines = []
    winning_amount = 0
    for lines in range(len(slots)):  #this loop will iterate equal to the length of the list or we can say slots
        first_symbol = slots[lines][0]  #store the 1st symbol of all rows
        for j in range(len(slots)):  
            if first_symbol!= slots[lines][j]: #compare with each and every value of row
                break
        else: #this else statement would be executed if and only if the if statement won't be true in any iteration
            winning_amount = winning_amount + (bet_value*values[first_symbol]) #simply we multiply the bet_amount on each line with the value of 
            winner_lines.append(lines+1) #save the line on which the bet is true
    return winner_lines , winning_amount
    
    
def game(deposit_amount):
    bet_line = bet_lines()
    
    while True:
        bet_amount_line = bet_amount()
        total_amount = bet_amount_line*bet_line  #total amount of bat
        if total_amount<=deposit_amount:
            break
        else:
            print(f"You entered the value which is greater than the deposit amount your total deposit is {int(deposit_amount)} so you can max enter the amount of ${int(deposit_amount/bet_line)}")
    print(f"You bet on each line ${bet_amount_line} and your total amount for bet is ${bet_amount_line*bet_line}")
    rows = slot_machine_random_symbols(ROWS,COLUMNS,symbol_counts)
    print_slot_machine_column(rows)
    columns = column(rows)
    winner_lines ,winning_amount , = winning(columns,bet_line,symbol_values,bet_amount_line)
    print(f"You won on {winner_lines}")
    print(f"The winning amount is {winning_amount}")     
    less_value = bet_amount_line*bet_line
    
    return less_value,total_amount,winning_amount,deposit_amount
    
def main():  #defining main function.
    deposit_amount = deposit_cash()
    print(deposit_amount)
    winning_amount = 0
    remain_amount_of_bat = deposit_amount
    while True:
        bet_lines = 
        remain_amount_of_bat =deposits_amount-total_amount_bat
        winning_amount = winnings_amount+winning_amount
        print(f"You have now ${remain_amount_of_bat}")
        inp = input("Do you wanna play again (yes/no): ").lower()
        if inp!="yes" or inp!="no":
            print("Enter a walid reply")
        elif inp=="yes":
            game(remain_amount_of_bat)
        elif inp=="no":
            break
        elif remain_amount_of_bat<least_value:
            break 
    print(f"The game has been ended and you won {winning_amount}")
    print(f"The reamining amout of bat is ${remain_amount_of_bat}")     

main()