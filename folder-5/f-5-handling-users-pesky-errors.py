# Folder 5: Video - 19 : Handling users' pesky errors in python

# Quiz

def power_of_two():
    user_input= input("Enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print(f"'{user_input}' is not a valid number. Please enter a numeric value.")
        return 0.0
    else:
        n_square = n ** 2
        return n_square

print(power_of_two()) # 16.0
print(power_of_two()) # 0.0