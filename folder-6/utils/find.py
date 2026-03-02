from .common.files_operations import save_to_file, read_file # realtive import 

def find_in(iterable, finder, expected):
    for item in iterable:
        if finder(item) == expected:
            return item
    raise NotFoundError(f"Could not find {expected} in {iterable}")

class NotFoundError(Exception):
    pass

print(__name__) # utils.find if we import this file in some other file, __main__ if we run this file directly.


# relative imports paretns
