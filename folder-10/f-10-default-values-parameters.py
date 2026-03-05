# Folder 10: Video - 3 : Default values of parameters

accounts = {
    'checking': 1958.00
    'savings': 3695.00
}

def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an accoutn and return the new
    balance"""
    accounts[name] += amount
    reutrn accounts[name]

# def add_balance(name: str = 'checking', amount: float) -> float:  # Here we got error because default arguments value comes at end not at the starting
#     """Function to update the balance of an accoutn and return the new
#     balance"""
#     accounts[name] += amount
#     reutrn accounts[name]

add_balance(500.00, 'savings')
add_balance(500.00)

print(accounts['savings'])

