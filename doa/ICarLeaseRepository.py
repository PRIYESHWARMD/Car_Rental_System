from abc import ABC, abstractmethod
from datetime import date

class ICarLeaseRepository(ABC):

    # Car Management
    @abstractmethod
    def add_car(self, vehicle): pass

    @abstractmethod
    def remove_car(self, vehicle_id): pass

    @abstractmethod
    def list_available_cars(self): pass

    @abstractmethod
    def list_rented_cars(self): pass

    @abstractmethod
    def find_car_by_id(self, vehicle_id): pass

    @abstractmethod
    def update_make(self,vehicle_id,make): pass

    @abstractmethod
    def update_model(self, vehicle_id,model): pass

    @abstractmethod
    def update_year(self, vehicle_id,year): pass

    @abstractmethod
    def update_daily_rate(self, vehicle_id,daily_rate): pass

    @abstractmethod
    def update_status(self, vehicle_id,status): pass

    @abstractmethod
    def update_engine_capacity(self, vehicle_id,engine_capacity): pass

    @abstractmethod
    def update_passenger_capacity(self, vehicle_id, passenger_capacity): pass

    ###################################################### Customer Management ##################################################
    # Customer Management
    @abstractmethod
    def add_customer(self, customer): pass

    @abstractmethod
    def remove_customer(self, customer_id): pass

    @abstractmethod
    def list_customers(self): pass

    @abstractmethod
    def find_customer_by_id(self, customer_id): pass

    @abstractmethod
    def update_phone_number(self,customer_id,phone_number):pass

    @abstractmethod
    def update_first_name(self,customer_id,first_name): pass

    @abstractmethod
    def update_last_name(self, customer_id, last_name): pass

    @abstractmethod
    def update_email(self, customer_id, email): pass

    ########################################################### Lease Management ###########################################################
    # Lease Management
    @abstractmethod
    def create_lease(self, customer_id: int, vehicle_id: int, start_date: date, end_date: date, lease_type: str): pass

    @abstractmethod
    def return_car(self, lease_id: int): pass

    @abstractmethod
    def list_active_leases(self): pass

    @abstractmethod
    def list_lease_history(self): pass

    @abstractmethod
    def get_lease_count_by_customer(self, customer_id): pass

    @abstractmethod
    def get_days_to_lease_end_by_car_id(self, car_id): pass

    @abstractmethod
    def find_lease_by_id(self, lease_id):pass

    @abstractmethod
    def calculate_lease_cost(self, vehicle_id, start_date, end_date, lease_type): pass

    @abstractmethod
    def get_customers_with_lease_counts(self): pass


    ############################################################# Payment Management ###############################################


    @abstractmethod
    def record_payment(self, lease_id: int, amount: float): pass

    @abstractmethod
    def get_payment_history_by_customer_id(self, customer_id):pass
