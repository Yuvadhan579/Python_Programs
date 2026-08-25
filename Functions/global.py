balance=100000
def deposit(amount):
    global balance
    balance+=amount
deposit(5000)
print("Balance=",balance)