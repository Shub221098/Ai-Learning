# Folder 6: Video - 11 :  Relative imports in python

# from utils.common.file_operations import save_to_file, read_file
# save_to_file('Charlie', 'data.txt')
# print(read_file('data.txt')) # It will print hello and Rolf both.

from utils.find import find_in
print(__name__) # __main__ if we run this file directly, utils.find if we import this file in some other file.

# utils.common.file_operations
# utils.find
# __main__