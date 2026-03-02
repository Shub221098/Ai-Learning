# Folder 5: Video - 6: Creating custom error in Python

class MyCustomError(TypeError):
    pass

raise MyCustomError() # __main__.MyCustomError
raise MyCustomError("OUCH! An error happend.") # __main__.MyCustomError: OUCH! An error happend.

class MyCustomError(TypeError):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

raise MyCustomError("OUCH! An error happend.", 500) # __main__.MyCustomError: ('OUCH! An error happend.', 500)

# Manage error code inside a string
class RuntimeErrorWithCode(Exception):
    """
    Exception raised when a specific error condition occurs.
    """
    def __init__(self, message, code):
        super().__init__(f"{message} (Error code: {code})")
        self.code = code

raise RuntimeErrorWithCode("OUCH! An error happend.", 500) # __main__.RuntimeErrorWithCode: OUCH! An error happend. (Error code: 500)

err = RuntimeErrorWithCode("OUCH! An error happend.", 500)
print(err.__doc__) # Exception raised when a specific error condition occurs.