from datetime import date, datetime
from .ICarLeaseRepository import ICarLeaseRepository
from entity.lease import Lease
from util.PropertyUtil import PropertyUtil
from entity.payment import Payment
from entity.customer import Customer
from entity.vehicle import Vehicle
from util.DBConnection import DBConnection
from exception.LeaseNotFoundException import LeaseNotFoundException
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerrNotFoundException import CustomerNotFoundException

class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.con=DBConnection.get_connection()
        self.con.autocommit=True

    def add_car(self, vehicle: Vehicle):
        cur = self.con.cursor()
        insert = """
            INSERT INTO Vehicle 
            (make, model, year, daily_rate, status, passenger_capacity, engine_capacity) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(insert, ( vehicle.get_make(),vehicle.get_model(),vehicle.get_year(),vehicle.get_daily_rate(),vehicle.get_status(),vehicle.get_passenger_capacity(),vehicle.get_engine_capacity()))
        vehicle_id = cur.lastrowid
        vehicle.set_vehicle_id(vehicle_id)
        cur.close()

    def remove_car(self, vehicle_id):
        cur=self.con.cursor()
        cur.execute("DELETE FROM Vehicle WHERE vehicle_id=%s",(vehicle_id,))
        if cur.rowcount==0:
            raise CarNotFoundException(f"Car with ID {vehicle_id} not found.")
        cur.close()

    def list_available_cars(self):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Vehicle WHERE status='available'")
        rows=cur.fetchall()
        cur.close()
        return [Vehicle(*row) for row in rows]

    def list_rented_cars(self):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Vehicle WHERE status <>'available'")
        rows= cur.fetchall()
        cur.close()
        return [Vehicle(*row) for row in rows]

    def find_car_by_id(self, vehicle_id):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Vehicle WHERE vehicle_id = %s",(vehicle_id,))
        row= cur.fetchone()
        cur.close()
        if not row:
            raise CarNotFoundException(f"Car with ID{vehicle_id}not found.")
        return Vehicle(*row)

    def update_make(self,vehicle_id,make):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        if not cur.fetchone():
            cur.close()
            raise CarNotFoundException(f"Car ID {vehicle_id} not found.")
        cur.execute("UPDATE vehicle SET make=%s Where vehicle_id=%s ", (make, vehicle_id,))
        cur.close()

    def update_model(self,vehicle_id,model):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        if not cur.fetchone():
            cur.close()
            raise CarNotFoundException(f"Car ID {vehicle_id} not found.")
        cur.execute("UPDATE vehicle SET model=%s Where vehicle_id=%s ", (model, vehicle_id,))
        cur.close()

    def update_year(self,vehicle_id,year):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        if not cur.fetchone():
            cur.close()
            raise CarNotFoundException(f"Car ID {vehicle_id} not found.")
        cur.execute("UPDATE vehicle SET year=%s Where vehicle_id=%s ", (year, vehicle_id,))
        cur.close()

    def update_daily_rate(self,vehicle_id,daily_rate):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        if not cur.fetchone():
            cur.close()
            raise CarNotFoundException(f"Car ID {vehicle_id} not found.")
        cur.execute("UPDATE vehicle SET daily_rate=%s Where vehicle_id=%s ", (daily_rate, vehicle_id,))
        cur.close()

    def update_status(self,vehicle_id,status):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        if not cur.fetchone():
            cur.close()
            raise CarNotFoundException(f"Car ID {vehicle_id} not found.")
        cur.execute("UPDATE vehicle SET status=%s Where vehicle_id=%s ", (status, vehicle_id,))
        cur.close()

    def update_engine_capacity(self,vehicle_id,engine_capacity):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        if not cur.fetchone():
            cur.close()
            raise CarNotFoundException(f"Car ID {vehicle_id} not found.")
        cur.execute("UPDATE vehicle SET engine_capacity=%s Where vehicle_id=%s ", (engine_capacity, vehicle_id,))
        cur.close()

    def update_passenger_capacity(self,vehicle_id,passenger_capacity):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        if not cur.fetchone():
            cur.close()
            raise CarNotFoundException(f"Car ID {vehicle_id} not found.")
        cur.execute("UPDATE vehicle SET passenger_capacity=%s Where vehicle_id=%s ", (passenger_capacity, vehicle_id,))
        cur.close()



    ###################################################### Customer Management ##################################################
    # -- Customer Management --

    def add_customer(self, customer:Customer):
        cur=self.con.cursor()
        insert="INSERT INTO Customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
        cur.execute(insert,(customer.get_first_name(),customer.get_last_name(),customer.get_email(),customer.get_phone_number()))
        customer_id=cur.lastrowid
        customer.set_customer_id(customer_id)
        cur.close()

    def remove_customer(self, customer_id):
        cur=self.con.cursor()
        cur.execute("DELETE FROM customer WHERE customer_id=%s",(customer_id,))
        if cur.rowcount()==0:
            raise CustomerNotFoundException(f"Customer id {customer_id} not found.")
        cur.close()

    def list_customers(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM customer")
        rows=cur.fetchall()
        cur.close()
        return [Customer(*row) for row in rows]

    def find_customer_by_id(self, customer_id):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM customer WHERE customer_id = %s",(customer_id,))
        row=cur.fetchone()
        cur.close()
        if not row:
            raise CustomerNotFoundException(f"Customer id {customer_id} not found")
        return Customer(*row)

    def update_phone_number(self,customer_id,phone_number):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM customer WHERE customer_id = %s", (customer_id,))
        if not cur.fetchone():
            cur.close()
            raise CustomerNotFoundException(f"Customer ID {customer_id} not found.")
        cur.execute("UPDATE customer SET phone_number=%s Where customer_id=%s ",(phone_number,customer_id,))
        cur.close()

    def update_first_name(self,customer_id,first_name):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM customer WHERE customer_id = %s", (customer_id,))
        if not cur.fetchone():
            cur.close()
            raise CustomerNotFoundException(f"Customer ID {customer_id} not found.")
        cur.execute("UPDATE customer SET first_name=%s Where customer_id=%s ",(first_name,customer_id,))
        cur.close()

    def update_last_name(self,customer_id,last_name):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM customer WHERE customer_id = %s", (customer_id,))
        if not cur.fetchone():
            cur.close()
            raise CustomerNotFoundException(f"Customer ID {customer_id} not found.")
        cur.execute("UPDATE customer SET last_name=%s Where customer_id=%s ",(last_name,customer_id,))
        cur.close()

    def update_email(self,customer_id,email):
        cur=self.con.cursor()
        cur.execute("SELECT 1 FROM customer WHERE customer_id = %s", (customer_id,))
        if not cur.fetchone():
            cur.close()
            raise CustomerNotFoundException(f"Customer ID {customer_id} not found.")
        cur.execute("UPDATE customer SET email=%s Where customer_id=%s ",(email,customer_id,))
        cur.close()

    ########################################################### Lease Management ###########################################################
    # -- Lease Management --


    def create_lease(self, customer_id, vehicle_id, start_date, end_date, lease_type):
        cur = self.con.cursor()


        if start_date < date.today():
            cur.close()
            raise ValueError("Start date cannot be in the past.")

        if end_date <= start_date:
            cur.close()
            raise ValueError("End date must be after the start date.")


        cur.execute("SELECT 1 FROM customer WHERE customer_id = %s", (customer_id,))
        if not cur.fetchone():
            cur.close()
            raise CustomerNotFoundException(f"No customer found with ID {customer_id}")


        cur.execute("SELECT daily_rate, status FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        result = cur.fetchone()
        if not result:
            cur.close()
            raise CarNotFoundException(f"No car found with ID {vehicle_id}")

        daily_rate, status = result
        if status.lower() != 'available':
            cur.close()
            raise Exception("Car is currently not available for lease.")
        delta = end_date - start_date
        if lease_type == 'daily':
            rental_amount = daily_rate * delta.days
        elif lease_type == 'monthly':
            months = max((delta.days // 30), 1)
            rental_amount = daily_rate * 30 * months
        else:
            cur.close()
            raise ValueError("Invalid lease type. Must be 'daily' or 'monthly'.")

        insert_query = """
            INSERT INTO lease (customer_id, vehicle_id, start_date, end_date, type, rental_amount)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (
            customer_id, vehicle_id, start_date, end_date, lease_type, rental_amount
        ))

        lease_id = cur.lastrowid


        cur.execute("UPDATE vehicle SET status = 'notavailable' WHERE vehicle_id = %s", (vehicle_id,))
        cur.close()
        return Lease(
            lease_id, vehicle_id, customer_id,
            start_date, end_date, lease_type, rental_amount
        )

    def return_car(self, lease_id: int):
        cur = self.con.cursor()
        cur.execute("""
            SELECT lease_id, vehicle_id, customer_id, start_date, end_date, type 
            FROM Lease WHERE lease_id=%s
        """, (lease_id,))
        row = cur.fetchone()

        if not row:
            cur.close()
            raise LeaseNotFoundException(f"Lease id {lease_id} not found")

        lease_id, vehicle_id, customer_id, start_date, end_date, lease_type, rental_amount = row

        cur.execute("UPDATE Vehicle SET status='available' WHERE vehicle_id=%s", (vehicle_id,))
        cur.close()

        return Lease(lease_id, vehicle_id, customer_id, start_date, end_date, lease_type,rental_amount)

    def list_active_leases(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM Lease WHERE end_date >= CURRENT_DATE")
        rows=cur.fetchall()
        cur.close()
        return [Lease(*row) for row in rows]

    def list_lease_history(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM Lease WHERE end_date < CURRENT_DATE")
        rows = cur.fetchall()
        cur.close()
        return [Lease(*row) for row in rows]

    def get_lease_count_by_customer(self, customer_id):
        cur = self.con.cursor()
        query = """
            SELECT c.customer_id, c.first_name, c.last_name, COUNT(l.lease_id) as lease_count
            FROM customer c
            LEFT JOIN lease l ON c.customer_id = l.customer_id
            WHERE c.customer_id = %s
            GROUP BY c.customer_id, c.first_name, c.last_name
        """
        cur.execute(query, (customer_id,))
        result = cur.fetchone()
        cur.close()
        return result

    def get_days_to_lease_end_by_car_id(self, car_id):
        cur = self.con.cursor()

        cur.execute("""
                        SELECT l.start_date, l.end_date, v.vehicle_id, v.make, v.model, v.year, v.daily_rate, 
                               v.status, v.passenger_capacity, v.engine_capacity
                        FROM lease l
                        JOIN vehicle v ON l.vehicle_id = v.vehicle_id
                        WHERE l.vehicle_id = %s AND l.end_date >= CURDATE()
                        ORDER BY l.end_date DESC
                        LIMIT 1
                    """, (car_id,))

        result = cur.fetchone()
        cur.close()

        if not result:
            return None

        start_date, end_date = result[0], result[1]
        days_left = (end_date - datetime.now().date()).days

        vehicle = Vehicle()
        vehicle.set_vehicle_id(result[2])
        vehicle.set_make(result[3])
        vehicle.set_model(result[4])
        vehicle.set_year(result[5])
        vehicle.set_daily_rate(result[6])
        vehicle.set_status(result[7])
        vehicle.set_passenger_capacity(result[8])
        vehicle.set_engine_capacity(result[9])

        return (days_left, start_date, end_date, vehicle)

    def find_lease_by_id(self, lease_id):
        cur = self.con.cursor()
        cur.execute("""
                    SELECT lease_id, vehicle_id, customer_id, start_date, end_date, type, rental_amount
                    FROM lease
                    WHERE lease_id = %s
                """, (lease_id,))
        row = cur.fetchone()
        cur.close()

        if row:
            lease_id, vehicle_id, customer_id, start_date, end_date, lease_type, rental_amount = row
            return Lease(lease_id, vehicle_id, customer_id, start_date, end_date, lease_type, rental_amount)
        else:
            raise LeaseNotFoundException(f"No lease found with ID {lease_id}")

    def calculate_lease_cost(self, vehicle_id, start_date, end_date, lease_type):
        cur = self.con.cursor()
        cur.execute("SELECT daily_rate FROM vehicle WHERE vehicle_id = %s", (vehicle_id,))
        result = cur.fetchone()
        cur.close()

        if not result:
                raise CarNotFoundException(f"No car found with ID {vehicle_id}")

        daily_rate = result[0]
        delta = (end_date - start_date).days

        if lease_type == 'daily':
            return daily_rate * delta
        elif lease_type == 'monthly':
            months = max(delta // 30, 1)
            return daily_rate * 30 * months
        else:
            raise ValueError("Lease type must be 'daily' or 'monthly'")

    def get_customers_with_lease_counts(self):
        cur = self.con.cursor()
        query = """
                    SELECT c.customer_id, c.first_name, c.last_name, COUNT(l.lease_id) as lease_count
                    FROM customer c
                    LEFT JOIN lease l ON c.customer_id = l.customer_id
                    GROUP BY c.customer_id, c.first_name, c.last_name
                    ORDER BY lease_count DESC
                """
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        return results




            ############################################################# Payment Management ###############################################

    # -- Payment Handling --

    def record_payment(self, lease_id: int, amount: float):
        cur = self.con.cursor()

        cur.execute("SELECT lease_id FROM Lease WHERE lease_id = %s", (lease_id,))
        if not cur.fetchone():
            cur.close()
            raise LeaseNotFoundException(f"Lease ID {lease_id} not found.")

        cur.execute("INSERT INTO Payment (lease_id, payment_date, amount) VALUES (%s, CURRENT_DATE, %s)",
                    (lease_id, amount))
        self.con.commit()
        cur.close()

    def get_payment_history_by_customer_id(self, customer_id):
        cur = self.con.cursor()
        query = """
            SELECT p.payment_id, p.lease_id, p.amount, p.payment_date
            FROM payment p
            INNER JOIN lease l ON p.lease_id = l.lease_id
            WHERE l.customer_id = %s
            ORDER BY p.payment_date DESC
        """
        cur.execute(query, (customer_id,))
        rows = cur.fetchall()
        cur.close()
        return rows
