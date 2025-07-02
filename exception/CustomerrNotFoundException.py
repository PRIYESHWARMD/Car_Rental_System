class CustomerNotFoundException(Exception):
    def __init__(self,message="Customer Id not found "):
        super().__init__(message)