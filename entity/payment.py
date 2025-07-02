class Payment:
    def __init__(self, payment_id=None, lease_id=None, payment_date=None, amount=None):
        self.__payment_id = payment_id
        self.__lease_id = lease_id
        self.__payment_date = payment_date
        self.__amount = amount

    def get_payment_id(self):
        return self.__payment_id
    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_lease_id(self):
        return self.__lease_id
    def set_lease_id(self, lease_id):
        self.__lease_id = lease_id

    def get_payment_date(self):
        return self.__payment_date
    def set_payment_date(self, payment_date):
        self.__payment_date = payment_date

    def get_amount(self):
        return self.__amount
    def set_amount(self, amount):
        self.__amount = amount
