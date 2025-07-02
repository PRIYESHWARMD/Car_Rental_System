class Vehicle:
    def __init__(self, vehicle_id=None, make=None, model=None, year=None, daily_rate=None, status=None, passenger_capacity=None, engine_capacity=None):
        self.__vehicle_id = vehicle_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__daily_rate = daily_rate
        self.__status = status
        self.__passenger_capacity = passenger_capacity
        self.__engine_capacity = engine_capacity

    # Getters and setters
    def get_vehicle_id(self):
        return self.__vehicle_id
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_make(self):
        return self.__make
    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year

    def get_daily_rate(self):
        return self.__daily_rate
    def set_daily_rate(self, daily_rate):
        self.__daily_rate = daily_rate

    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

    def get_passenger_capacity(self):
        return self.__passenger_capacity
    def set_passenger_capacity(self, passenger_capacity):
        self.__passenger_capacity = passenger_capacity

    def get_engine_capacity(self):
        return self.__engine_capacity
    def set_engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity
