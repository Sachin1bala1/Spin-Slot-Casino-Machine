import random

MAX_LINES = 3
MAX_BET=100
MIN_BET=1

ROWS, COLS = 3, 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A":10,
    "B":7,
    "C":5,
    "D":3
}
def check_winnings(columns,lines,bet,values):
    winning=0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winning+=values[symbol]*bet
            winning_lines.append(line+1)
    return winning,winning_lines

def get_slot_machine_spint(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy only
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Enter the number.")
    return amount
def get_number_of_lines():
    while True:
        lines=input("Enter the no of lines to bet on(1-"+str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines = int(lines)
            if lines>0 and lines<=MAX_LINES:
                break
            else:
                print("amount must be greater than 0 and less than"+str(MAX_LINES)+".")
        else:
            print("Enter the number.")
    return lines

def get_bet():
    while True:
        amount=input("What amount would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET :
                break
            else:
                print(f"amount must be between ${MIN_BET} -${MAX_BET}")
        else:
            print("Enter the number.")
    return amount
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row])
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You do not have enough to bet. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.Total bet amount is equal to: ${total_bet}")

    slots = get_slot_machine_spint(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on", *winning_line)
    return winnings-total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your total balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        profit = spin(balance)
        balance += profit
        if balance==0:
            print("You are out of money.")
            break
    print(f"Your total balance is ${balance}")

main()

