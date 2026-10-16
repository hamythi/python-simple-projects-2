#name, balance
#empty and transfer to new savign acct 
# select bank1
# show balance of bank1
# select bank2
# show balance of bank2
# select transaction action
# select amount
# show result balance of bank1
# show result balance of bank2
# avoid overdraft

# 1. The accounting system should take care of 5 types of accounts and also make transactions debit, credit based instead of simple increment decrement
# 2. The ledger should be date range based

bank_rec = {"ew": 1600, "wf": 4000, "wf_saving": 500, "boa": 2500, "us": 3400, "ew_savings": 0}
actions = ["send", "request", "exit", "history"]
ledger = {} #trans_id, prior, result

def send():
    bank_sel1 = input("Select Bank 1: ").lower()
    if bank_sel1 in bank_rec:
        print(f"Current balance: {bank_rec[bank_sel1]}")
    bank_sel2 = input("Select Bank 2: ").lower()
    if bank_sel2 in bank_rec:
        print(f"Current balance: {bank_rec[bank_sel2]}")
    amount = int(input("Enter amount you wish to send: "))
    if bank_rec[bank_sel1] < amount:
        print("Overdraft! Amount larger than current balance. Please enter a smaller amount")
    bank_rec[bank_sel1] -= amount
    bank_rec[bank_sel2] += amount
    transaction = f"New balance for {bank_sel1}: {bank_rec[bank_sel1]}; New balance for {bank_sel2}: {bank_rec[bank_sel2]}"
    print(transaction)
    ledger["Bank"] = [f"{bank_sel1}", f"{bank_sel2}"]
    ledger["Amount"] = [f"-{amount}", f"+{amount}"]
    ledger["New Balance"] = [f"{bank_rec[bank_sel1]}", f"{bank_rec[bank_sel2]}"]
    print(f'{ledger["Bank"][-1]} \n {ledger["Amount"][-1]} \n {ledger["New Balance"][-1]}')
    print(f'{ledger["Bank"][-2]} \n {ledger["Amount"][-2]} \n {ledger["New Balance"][-2]}')
        
def request():
    bank_sel1 = input("Select Bank 1: ").lower()
    if bank_sel1 in bank_rec:
        print(f"Current balance: {bank_rec[bank_sel1]}")
    bank_sel2 = input("Select Bank 2: ").lower()
    if bank_sel2 in bank_rec:
        print(f"Current balance: {bank_rec[bank_sel2]}")
    amount = int(input("Request amount: "))
    if bank_rec[bank_sel2] < amount:
        print("Overdraft! Amount larger than current balance. Please enter a smaller amount")
    bank_rec[bank_sel1] += amount
    bank_rec[bank_sel2] -= amount
    transaction = f"New balance for {bank_sel1}: {bank_rec[bank_sel1]}; New balance for {bank_sel2}: {bank_rec[bank_sel2]}"
    print(transaction)
    ledger["Bank"] = [f"{bank_sel1}", f"{bank_sel2}"]
    ledger["Amount"] = [f"+{amount}", f"-{amount}"]
    ledger["New Balance"] = [f"{bank_rec[bank_sel1]}", f"{bank_rec[bank_sel2]}"]
    print(f'{ledger["Bank"][-1]} \n {ledger["Amount"][-1]} \n {ledger["New Balance"][-1]}')
    print(f'{ledger["Bank"][-2]} \n {ledger["Amount"][-2]} \n {ledger["New Balance"][-2]}')

def trans_trak():
    print(actions)
    while True:
        act = input("What would you like to do? ").lower()
        if act == "exit":
            break
        elif act == "send":
            send()
        elif act == "request":
            request()
        elif act == "history":
            choose_bank = input("Bank name: ").lower()
            i = ledger["Bank"].index(choose_bank)
            print(ledger["Bank"][i])

print(ledger)
trans_trak()
