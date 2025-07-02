import unittest
from datetime import date, timedelta
from doa.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.lease import Lease
from entity.payment import Payment
from entity.customer import Customer
from entity.vehicle import Vehicle
from exception.LeaseNotFoundException import LeaseNotFoundException
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerrNotFoundException import CustomerNotFoundException

class TestCarLeaseSystem(unittest.TestCase):

    def setUp(self):
        self.impl = ICarLeaseRepositoryImpl()


        conn = self.impl.con
        cur = conn.cursor()

        cur.execute("DELETE FROM Payment")
        cur.execute("DELETE FROM Lease")
        cur.execute("DELETE FROM Vehicle")
        cur.execute("DELETE FROM Customer")
        conn.commit()
        cur.close()

    def test_add_car_success(self):
        vehicle = Vehicle(None, "Toyota", "Camry", 2020, 55.0, "available", 5, 2.5)
        self.impl.add_car(vehicle)
        self.assertIsNotNone(vehicle.get_vehicle_id())

    def test_create_lease_success(self):
        customer = Customer(None, "John", "Doe", "john@example.com", "1234567890")
        self.impl.add_customer(customer)

        vehicle = Vehicle(None, "Honda", "Civic", 2022, 60.0, "available", 5, 1.8)
        self.impl.add_car(vehicle)

        lease = self.impl.create_lease(
            customer.get_customer_id(),
            vehicle.get_vehicle_id(),
            date.today(),
            date.today() + timedelta(days=5),
            "daily"
        )
        self.assertIsNotNone(lease.get_lease_id())

    def test_retrieve_lease_success(self):
        customer = Customer(None, "Jane", "Smith", "jane@example.com", "0987654321")
        self.impl.add_customer(customer)

        vehicle = Vehicle(None, "Ford", "Focus", 2021, 50.0, "available", 5, 2.0)
        self.impl.add_car(vehicle)

        lease = self.impl.create_lease(
            customer.get_customer_id(),
            vehicle.get_vehicle_id(),
            date.today(),
            date.today() + timedelta(days=5),
            "monthly"
        )

        leases = self.impl.list_active_leases()
        lease_ids = [l.get_lease_id() for l in leases]
        self.assertIn(lease.get_lease_id(), lease_ids, "Lease should be listed in active leases")

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            self.impl.find_customer_by_id(-999)

    def test_car_not_found_exception(self):
        with self.assertRaises(CarNotFoundException):
            self.impl.find_car_by_id(-999)

    def test_lease_not_found_exception(self):
        with self.assertRaises(LeaseNotFoundException):
            self.impl.return_car(-999)


if __name__ == "__main__":
    unittest.main()
