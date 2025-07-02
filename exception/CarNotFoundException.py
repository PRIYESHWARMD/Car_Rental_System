class CarNotFoundException(Exception):
    def __init__(self,message="Car Id is not found"):
        super().__init__(message)