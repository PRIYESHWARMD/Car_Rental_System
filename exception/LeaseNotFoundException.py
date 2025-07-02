class LeaseNotFoundException(Exception):
    def __init__(self,message="Lease Id is not found"):
        super().__init__(message)
