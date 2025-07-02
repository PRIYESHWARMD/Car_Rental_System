class Lease:
    def __init__(self, lease_id, vehicle_id, customer_id, start_date, end_date, lease_type, rental_amount):
        self.lease_id = lease_id
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.start_date = start_date
        self.end_date = end_date
        self.lease_type = lease_type
        self.rental_amount = rental_amount

    def get_lease_id(self):
        return self.lease_id
    def get_vehicle_id(self):
        return self.vehicle_id
    def get_customer_id(self):
        return self.customer_id
    def get_start_date(self):
        return self.start_date
    def get_end_date(self):
        return self.end_date
    def get_lease_type(self):
        return self.lease_type
    def get_rental_amount(self):
        return self.rental_amount
