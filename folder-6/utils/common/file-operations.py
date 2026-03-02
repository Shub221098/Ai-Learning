# Folder 6: Video - 10 :  importing own python files
from ..find import NotFoundError # for relative import parents

def save_to_file(filename, data):
    with open(filename,'w') as file:
        file.write(data)

def read_file(filename):
    with open(filename,'r') as file:
        return file.read() # 'Rolf\nCharlie\nAnna\nJen'.split('\n')  ['Rolf', 'Charlie', 'Anna', 'Jen']


print(__name__) # __main__ if we run this file directly, utils.common.file_operations if we import this file in some other file.