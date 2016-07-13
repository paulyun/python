customers = ["MIKE", "JANE", "STEVE"]
balances = [300, 300, 300]

username = input("Please enter your first name: ").upper()
while username not in customers:
    print("Please enter a first name on the approved list!")
    username  = input("Please enter your first name: ").upper()
    
def deposit_function(y):
    if username == "MIKE":
        balances[0] = balances[0] + y
    if username == "JANE":
        balances[1] = balances[1] + y
    if username == "STEVE":
        balances[2] = balances[2] + y
    
def withdraw_function(y):
    if username == "MIKE":
        balances[0] = balances[0] - y
    if username == "JANE":
        balances[1] = balances[1] - y
    if username == "STEVE":
        balances[2] = balances[2] - y
        
def balance_function():
    if username == "MIKE":
        print("Your account balance is: ", balances[0])
    if username == "JANE":
        print("Your account balance is: ", balances[1])
    if username == "STEVE":
        print("Your account balance is: ", balances[2])
        
def username_function():
    global username
    username = input("Please enter your first name: ").upper()
    while username not in customers:
        print("Please enter a first name on the approved list!")
        username  = input("Please enter your first name: ").upper()

user_input = ""
while user_input != "E":
    user_input = input("\n Input D to Deposit \n Input W to Withdraw \n Input B to Display Balance \n Input C to Change User \n Input E to Exit Program ").upper()
    if user_input == "D":
        deposit = float(input("Please enter the amount you want to deposit: "))
        deposit_function(deposit)
        balance_function()
    elif user_input == "W":
        balance_function()
        withdraw = float(input("Please enter the amount you want to withdraw: "))
        withdraw_function(withdraw)
        balance_function()
    elif user_input == "B":
        balance_function()
    elif user_input == "C":
        username_function()