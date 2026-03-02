# Folder 9: Video - 3 : Generators & Iterable in python


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < 100:
            current_number = self.number
            self.number += 1
            return current_number
        else:
            raise StopIteration

my_gen = FirstHundredGenerator()
print(my_gen) # <__main__.FirstHundredGenerator object at 0x000
print(my_gen.number) # 0
print(next(my_gen)) # 1

for i in my_gen:
    print(i) # 2, 3, 4, 5, ..., 99


class FirstFiveIterator:
    def __init__(self):
        self.number = [1, 2, 3, 4, 5]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.number):
            current_number = self.number[self.i]
            self.i += 1
            return current_number
        else:
            raise StopIteration