# Folder 1: Video - 12 : Getting user input in Python

my_name = "Jose"
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {my_name}.")

# If we type a number in input it will be string so for below case will get wrong multiplication
age = input("Enter your age: ")
# another way to convert age into integer 
age = int(input("ENter your age: "))
print(f"You have lived for {age * 12} months.") # YOu have lived for 36 months.
months = age * 12
print(f"You have lived for {months} months.")

age_num = int(age) # to perfectly multiply and get answer
print(f"You have lived for {age * 12} months.") # YOu have lived for 33333333 months.
print(f"You have lived for {age_num * 12} months.") # YOu have lived for 36 months.


