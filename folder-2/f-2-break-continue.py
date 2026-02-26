# Folder 2: Video - 7 : Break and Continue

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

# break will get out of the loop no further run of code
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")

# Continue will get out of current iternation and go to next one
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...!")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!")


# Folder 2: Video - 8 : Else keyword with loops
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

# Here it is not necessary to write if for else statement it works with loops and print else part when remove "faulty" from string
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        all_successful = False
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    print("All card build successfully. No faulty cars!")


