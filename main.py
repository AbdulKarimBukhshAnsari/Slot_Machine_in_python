import random




#global_variables
MAX__LINES = 3
MIN__LINES = 1
MAX__BET = 1000
ROWS = 3
COLUMNS = 3
symbol_counts = {"A":3,"B":5,"C":7,"D":9}  #the symbols which will appear on slot machine
symbol_values = {"A":9,"B":7,"C":5,"D":3}  #the values of each symbol. 



def slot_machine_random_symbols(rows,columns,symbols): #make the matrices of slot machine.
    whole_symbols= [symbol for symbol,symbol_count in symbols.items()  for i in range(symbol_count)] #used list comprehension to store the symbols depends upon their frequency
    slot_machine = []
    for i in range(rows):
        row = []
        all_symbols = whole_symbols[:] #make the copy of the list so that the real list won't be changed we put inside the for loop so that in every iteration of outer loop the same list will be copied.
        for j in range(columns):   #this loop will iterate until and unless the columns will be completed
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
            if  MIN__LINES<=lines<=MAX__LINES:                
                break
            else:
                print(f"Enter the value in between {MIN__LINES} and {MAX__LINES} inclusively. ")
        else:
            print("Enter a valid number.")
            
    return lines       
            
def bet_amount_line():
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
    for i in range(lines):  #this loop will iterate equal to the length of the list or we can say slots
        first_symbol = slots[i][0]  #store the 1st symbol of each rows.
        for j in range(len(slots)):  
            if first_symbol!= slots[i][j]: #compare with each and every value of row
                break
        else: #this else statement would be executed if and only if the if statement won't be true in any iteration
            winning_amount = winning_amount + (bet_value*values[first_symbol]) #simply we multiply the bet_amount on each line with the value of 
            winner_lines.append(i+1) #save the line on which the bet is true
    return winner_lines , winning_amount
    
    


def main(): #defining the main function
    deposit_amount = deposit_cash()  
    winning_amount = 0 #intilaize the winning varible with zero.
    remain_value = deposit_amount

    
    while True:
        inp = input("Do yo wanna play the game (yes/no): ").lower() #ask the user if you wanna play.
       
        if inp=="yes":            
            while True:
                
                bet_line = bet_lines()
                bet_amount_li = bet_amount_line()
                total_amount = bet_amount_li*bet_line  #total amount of bat
                
                if total_amount<=deposit_amount: #check if you have enough amount or not if it is than it will break the loop.
                    break
                else:
                    print(f"You entered the value which is greater than the deposit amount your total deposit is {int(remain_value)} so you can max enter the amount of ${int(remain_value/bet_line)}")
            
            if remain_value<total_amount:  #will continue to be executed until and unless the remaining value as compare to the total amount foe global.
                print("You don't have enough credit to bet again so the game  end... ") 
                break
            
            if remain_value<total_amount:
                print("You don't have enough credit to bet again so the game  end... ") 
                break
            print(f"You bet on each line ${bet_amount_li} and total amount of bet is ${total_amount}. ")
            rows = slot_machine_random_symbols(ROWS,COLUMNS,symbol_counts) #make the random matrices of the slot
            print_slot_machine_column(rows) #transpose the matrices 
            columns = column(rows)       #store that matix
            winner_lines ,winning_amount_bet , = winning(columns,bet_line,symbol_values,bet_amount_li)   #check how many times the user has winned the bet in each turn.
            winning_amount += winning_amount_bet  #add the winning value in winner amount
            remain_value-=total_amount # less the value from deposit amount which is allready used in bet.
            
            print(f"You won on this turn ${winning_amount_bet} \nand you won on {tuple(winner_lines) } lines")
            print(f"\nYou have totally won ${winning_amount} and the remaining value is ${remain_value} ")
        elif inp =="no":
            print("The game has been ended")
            break
        
        else:
            print("Invalid choice kindly give your naswer in (yes/no)")
            continue
    print(f"The total winning amount is ${winning_amount}")
    print(f"The remaining amount is {remain_value} ")
    print("____________Thank you for playing this game______________")
    
main()                    
            