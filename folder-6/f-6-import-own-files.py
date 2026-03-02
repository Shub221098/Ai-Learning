# Folder 6: Video - 10 :  importing own python files

import file_operations

file_operations.save_to_file('Rolf', 'data.txt')
print(file_operations.read_file('data.txt'))

# other way to import 

from file_operations import save_to_file, read_file
save_to_file('Charlie', 'data.txt')
print(read_file('data .txt'))

# if file_operations is inside utils then we need to import like

from utils.file_operations import save_to_file, read_file
save_to_file('Charlie', 'data.txt')
print(read_file('data.txt'))
