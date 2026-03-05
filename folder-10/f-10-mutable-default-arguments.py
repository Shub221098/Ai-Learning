# Folder 10: Video - 4 : Mutable Default arguments

def create_account(name: str, holder: str, account_holders: list = []):
    print(id(account_holders))
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }

a1 = create_account('checking', 'Rolf') # same id comes
a2 = create_account('savings', 'Jen') # same id comes

print(a2) #  { 'name': 'savings', 'main_account_holder': 'Jen', 'account_holders': ['Rolf', 'Jen'] }

# why rolf jen comes in a2 we didnt add Rolf, it is because default [] is created when the function is created not when function is called
# 1-way:  to resolve this remove default value and add [] in function calling
# 2-way: make default value to account_holders = None
# if not account_holders:
#   account_holders = []
