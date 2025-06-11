#Dictionary to store account ballances for multiple users
account_balances = {(1023, 'John Mark'): 3000.0, (1024, 'Stacy Kanini'): 789000.0, (1025, 'Charles Brown'): 600.0, (1026, 'Amelia Dimoldenberg'): 48.0}

#deposit money into your account
def deposit_money(account_no, amount):
    if account_no not in account_balances:
        print("Account does not exist")
    for account in account_balances:
        if account[0] == account_no:
            account_balances[account] += amount
            print(f"Succesfully deposited {amount} shillings into account {account_no}. New balance: {account_balances[account]}")
        

#withdraw money
def withdraw_money(account_no, amount):
    if account_no not in account_balances:
        print("Account does not exist")
    for account in account_balances:
        if account[0] == account_no:
            if account_balances[account] < amount:
                print(f"Cannot process request due to insufficient funds in account {account_no}.")
            else:
                account_balances[account] -= amount
                print(f"Succesfully withdrawn {amount} shillings from account {account_no}. New balance: {account_balances[account]}")
        
def transfer_money(from_account_no, to_account_no, amount):
    # Find the keys matching the given account numbers
    from_account_key = None
    to_account_key = None

    for key in account_balances:
        if key[0] == from_account_no:
            from_account_key = key
        if key[0] == to_account_no:
            to_account_key = key

    if from_account_key is None:
        print(f"Account {from_account_no} does not exist.")
        return
    if to_account_key is None:
        print(f"Account {to_account_no} does not exist.")
        return

    if account_balances[from_account_key] < amount:
        print(f"Insufficient funds in account {from_account_no}.")
        return

    # Transfer the funds
    account_balances[from_account_key] -= amount
    account_balances[to_account_key] += amount
    print(f"Transferred {amount} from {from_account_key[1]} to {to_account_key[1]}.")
    print(f"New balance for {from_account_key[1]}: {account_balances[from_account_key]}")
    print(f"New balance for {to_account_key[1]}: {account_balances[to_account_key]}")


transfer_money(1023, 1024, 500.0)