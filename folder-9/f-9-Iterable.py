# Folder 9: Video - 5 : Iterables in python

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    # The __iter__ method returns the iterator object itself. This is a requirement for an object to be an iterator.
    def __iter__(self):
        return self

    # The __next__ method returns the next value from the iterator. If there are no more items to return, it raises a StopIteration exception.
    def __next__(self):
        if self.number < 100:
            current_number = self.number
            self.number += 1
            return current_number
        else:
            raise StopIteration

class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

print(sum(FirstHundredIterable())) # 4950

for i in FirstHundredIterable():
    print(i) # 0, 1, 2, 3, ..., 99

# class AnotherIterable:
#     def __iter__(self):
#         self.cars = ['Ford', 'BMW', 'Audi']
        
#     def __len__(self):
#         return len(self.cars)
    
#     def __getitem__(self, index):
#         return self.cars[index]

# for car in AnotherIterable():
#     print(car) # Ford, BMW, Audi

my_numbers =[x for x in [1, 2, 3, 4, 5]] # list comprehension
my_numbers_gen = (x for x in [1, 2, 3, 4, 5]) # generators comprehension object

print(next(my_numbers_gen))