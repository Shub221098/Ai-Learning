# Folder 1: Video - 22 : length and sum

grades = [80, 75, 90 ,100]
total = sum(grades) # we can add list, tuple, set anythign

length = len(grades)

average = total / length
print(average)


# Example below scenarion not best for grades
grades = [80, 75, 90 ,100] # it allows all the flexibility
grades = {80, 75, 90 ,100} # it is also not good because if we put again 100 then it is not added in set
grades = (80, 75, 90 ,100) # not good because we can't add more grades directly

# Folder 1: Video - 23 : Joining a list

friends = ["Rolf", "Anne", "Charlie"]
comma_seperated = ", ".join(friends)
print(f"My friends are {comma_seperated}.") # My friennds are Rolf, Anne, Charlie.
