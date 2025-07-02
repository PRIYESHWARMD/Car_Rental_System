from datetime import date, datetime
import re
from doa.ICarLeaseRepository import ICarLeaseRepository
from doa.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.lease import Lease
from entity.payment import Payment
from entity.customer import Customer
from entity.vehicle import Vehicle
from util.DBConnection import DBConnection
from util.PropertyUtil import PropertyUtil
from exception.LeaseNotFoundException import LeaseNotFoundException
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerrNotFoundException import CustomerNotFoundException
from tabulate import tabulate

def car_management_menu(impl):
    while True:
        print("\n--- Car Management ---")
        print("1. Add Car")
        print("2. Delete Car")
        print("3. Update or Edit")
        print("4. List Available Cars")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                car = Vehicle()
                make = input("Enter Make: ").strip()
                if not make:
                    raise ValueError("Make cannot be empty.")
                car.set_make(make)
                model = input("Enter Model: ").strip()
                if not model:
                    raise ValueError("Model cannot be empty.")
                car.set_model(model)

                year = int(input("Enter Year: "))
                current_year = datetime.now().year
                if year < 1950 or year > current_year:
                    raise ValueError("Year must be between 1950 and current year.")
                car.set_year(year)

                daily_rate = float(input("Enter daily rate: "))
                if daily_rate <= 0:
                    raise ValueError("Daily rate must be positive.")
                car.set_daily_rate(daily_rate)

                car.set_status("available")

                capacity = int(input("Enter passenger capacity: "))
                if capacity <= 0:
                    raise ValueError("Passenger capacity must be positive.")
                car.set_passenger_capacity(capacity)

                engine = float(input("Enter engine capacity: "))
                if engine <= 0:
                    raise ValueError("Engine capacity must be positive.")
                car.set_engine_capacity(engine)

                impl.add_car(car)
                print(f"Car added successfully. Car ID is {car.get_vehicle_id()}.")

            except Exception as e:
                print(f"Failed to add car: {e}")

        elif choice == '2':
            try:
                car_id = int(input("Enter Car ID to delete: "))
                impl.remove_car(car_id)
                print("Car deleted.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                car_id = int(input("Enter your Car ID: "))
                car = impl.find_car_by_id(car_id)

                print("\nCurrent Car Info:")
                headers = ["Vehicle ID", "Make", "Model", "Year", "Daily Rate", "Status", "Passenger Capacity",
                           "Engine Capacity"]
                table = [[
                    car.get_vehicle_id(),
                    car.get_make(),
                    car.get_model(),
                    car.get_year(),
                    car.get_daily_rate(),
                    car.get_status(),
                    car.get_passenger_capacity(),
                    car.get_engine_capacity()
                ]]
                print(tabulate(table, headers=headers, tablefmt="grid"))

                while True:
                    print("\n--- Update Options ---")
                    print("1. Update Make")
                    print("2. Update Model")
                    print("3. Update Year")
                    print("4. Update Daily Rate")
                    print("5. Update Status")
                    print("6. Update Passenger Capacity")
                    print("7. Update Engine Capacity")
                    print("8. Back")

                    option = input("Enter your choice: ")

                    try:
                        if option == '1':
                            make = input("Enter New Make: ").strip()
                            if not make:
                                raise ValueError("Make cannot be empty.")
                            impl.update_make(car_id, make)

                        elif option == '2':
                            model = input("Enter New Model: ").strip()
                            if not model:
                                raise ValueError("Model cannot be empty.")
                            impl.update_model(car_id, model)

                        elif option == '3':
                            year = int(input("Enter New Year: "))
                            current_year = datetime.now().year
                            if year < 1950 or year > current_year:
                                raise ValueError("Year must be between 1950 and current year.")
                            impl.update_year(car_id, year)

                        elif option == '4':
                            rate = float(input("Enter New Daily Rate: "))
                            if rate <= 0:
                                raise ValueError("Daily rate must be positive.")
                            impl.update_daily_rate(car_id, rate)

                        elif option == '5':
                            status = input("Enter New Status (available/unavailable): ").strip().lower()
                            if status not in ['available', 'unavailable']:
                                raise ValueError("Status must be 'available' or 'unavailable'.")
                            impl.update_status(car_id, status)

                        elif option == '6':
                            capacity = int(input("Enter New Passenger Capacity: "))
                            if capacity <= 0:
                                raise ValueError("Passenger capacity must be positive.")
                            impl.update_passenger_capacity(car_id, capacity)

                        elif option == '7':
                            engine = float(input("Enter New Engine Capacity: "))
                            if engine <= 0:
                                raise ValueError("Engine capacity must be positive.")
                            impl.update_engine_capacity(car_id, engine)

                        elif option == '8':
                            break
                        else:
                            print("Invalid choice. Try again.")
                            continue

                        print("Update completed.")

                    except Exception as e:
                        print(f"Validation Error: {e}")

            except CarNotFoundException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Update failed: {e}")


        elif choice == '4':
            cars = impl.list_available_cars()
            if not cars:
                print("No available cars.")
            else:
                headers = ["Vehicle ID", "Make", "Model", "Year", "Daily Rate", "Status", "Passenger Capacity",
                           "Engine Capacity"]
                table = []
                for car in cars:
                    table.append([
                        car.get_vehicle_id(),
                        car.get_make(),
                        car.get_model(),
                        car.get_year(),
                        car.get_daily_rate(),
                        car.get_status(),
                        car.get_passenger_capacity(),
                        car.get_engine_capacity()
                    ])

                print(tabulate(table, headers=headers, tablefmt="grid"))

        elif choice == '5':
            break
        else:
            print("Invalid option. Try again.")


###################################################### Customer Management ##################################################
def customer_management_menu(impl):
    while True:
        print("\n--- Customer Management ---")
        print("1. Add Customer")
        print("2. Delete Customer")
        print("3. Update Phone Number")
        print("4. List of Customers")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            customer = Customer()
            while True:
                first_name = input("Enter first name: ").strip()
                if first_name.isalpha():
                    customer.set_first_name(first_name)
                    break
                else:
                    print("First name must contain only letters.")
            while True:
                last_name = input("Enter last name: ").strip()
                if last_name.isalpha():
                    customer.set_last_name(last_name)
                    break
                else:
                    print("Last name must contain only letters.")
            while True:
                email = input("Enter email: ").strip()
                if email.endswith("@gmail.com") and re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email):
                    customer.set_email(email)
                    break
                else:
                    print("Invalid email. It must be a valid Gmail address (e.g., example@gmail.com).")
            while True:
                phone = input("Enter phone number: ").strip()
                if phone.isdigit() and 7 <= len(phone) <= 15:
                    customer.set_phone_number(phone)
                    break
                else:
                    print("Phone number must contain only digits and be 7-15 characters long.")
            impl.add_customer(customer)
            print(f"Customer added successfully and your Id is {customer.get_customer_id()}.")

        elif choice == '2':
            customer_id = int(input("Enter Customer ID to delete: "))
            impl.remove_customer(customer_id)
            print("Customer deleted.")



        elif choice == '3':
            try:
                customer_id = int(input("Enter your customer ID: "))
                customer = impl.find_customer_by_id(customer_id)
                headers = ["Customer ID", "First Name", "Last Name", "Email", "Phone Number"]
                table = [[
                    customer.get_customer_id(),
                    customer.get_first_name(),
                    customer.get_last_name(),
                    customer.get_email(),
                    customer.get_phone_number()
                ]]
                print("\nCurrent Customer Info:")
                print(tabulate(table, headers=headers, tablefmt="grid"))

                while True:
                    print("\n--- Update Options ---")
                    print("1. Update First Name")
                    print("2. Update Last Name")
                    print("3. Update Email")
                    print("4. Update Phone Number")
                    print("5. Back")
                    option = input("Enter your choice: ")
                    if option == '1':
                        first_name = input("Enter New First Name: ").strip()
                        if not first_name or not first_name.replace(" ", "").isalpha():
                            print("Invalid first name. Only letters are allowed and it can't be empty.")
                        else:
                            impl.update_first_name(customer_id, first_name)
                            print("First name updated successfully.")
                    elif option == '2':
                        last_name = input("Enter New Last Name: ").strip()
                        if not last_name or not last_name.replace(" ", "").isalpha():
                            print("Invalid last name. Only letters are allowed and it can't be empty.")
                        else:
                            impl.update_last_name(customer_id, last_name)
                            print("Last name updated successfully.")
                    elif option == '3':
                        email = input("Enter New Email: ").strip()
                        if not email.endswith("@gmail.com"):
                            print("Invalid email. Only '@gmail.com' addresses are accepted.")
                        else:
                            impl.update_email(customer_id, email)
                            print("Email updated successfully.")
                    elif option == '4':
                        phone = input("Enter New Phone Number: ").strip()
                        if not phone.isdigit() or len(phone) < 10:
                            print("Invalid phone number. Must be at least 10 digits.")
                        else:
                            impl.update_phone_number(customer_id, phone)
                            print("Phone number updated successfully.")
                    elif option == '5':
                        break
                    else:
                        print("Invalid choice. Try again.")
            except CustomerNotFoundException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Update failed: {e}")
        elif choice == '4':
            customers = impl.list_customers()
            if not customers:
                print("No customers found.")
            else:
                headers = ["Customer ID", "First Name", "Last Name", "Email", "Phone Number"]
                table = []
                for customer in customers:
                    table.append([
                        customer.get_customer_id(),
                        customer.get_first_name(),
                        customer.get_last_name(),
                        customer.get_email(),
                        customer.get_phone_number()
                    ])
                print(tabulate(table, headers=headers, tablefmt="grid"))

        elif choice == '5':
            break
        else:
            print("Invalid option. Try again.")

########################################################### Lease Management ###########################################################
def lease_management_menu(impl):
    while True:
        print("\n--- Lease Management ---")
        print("1. Create Lease")
        print("2. Return Car")
        print("3. List Active Leases")
        print("4. List Lease History")
        print("5. Get Customer Lease Count")
        print("6. Days to Lease End by Car ID")
        print("7. Calculate Lease Cost")
        print("8. Customer with No of Lease")
        print("9. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                cid = int(input("Enter Customer ID: "))
                vid = int(input("Enter Car ID: "))
                start_str = input("Enter start date (YYYY-MM-DD): ")
                end_str = input("Enter end date (YYYY-MM-DD): ")
                lease_type = input("Enter lease type (daily/monthly): ").lower()

                if lease_type not in ['daily', 'monthly']:
                    print("Invalid lease type. Must be 'daily' or 'monthly'.")
                    continue

                try:
                    start_date = datetime.strptime(start_str, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_str, '%Y-%m-%d').date()
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD.")
                    continue

                today = date.today()
                if start_date < today:
                    print("Start date cannot be in the past.")
                    continue
                if end_date <= start_date:
                    print("End date must be after the start date.")
                    continue

                lease = impl.create_lease(cid, vid, start_date, end_date, lease_type)
                print(f"Lease created with ID: {lease.get_lease_id()}")

            except (CustomerNotFoundException, CarNotFoundException) as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Failed to create lease: {e}")

        elif choice == '2':
            try:
                lease_id = int(input("Enter Lease ID to return: "))
                lease = impl.return_car(lease_id)
                print(f"Returned car with Vehicle ID {lease.get_vehicle_id()} for Customer ID {lease.get_customer_id()}")
            except LeaseNotFoundException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Failed to return car: {e}")

        elif choice == '3':
            leases = impl.list_active_leases()
            if not leases:
                print("No active leases found.")
            else:
                headers = ["Lease ID", "Customer ID", "Vehicle ID", "Start Date", "End Date", "Lease Type"]
                table = [
                    [lease.get_lease_id(), lease.get_customer_id(), lease.get_vehicle_id(),
                     lease.get_start_date(), lease.get_end_date(), lease.get_lease_type()]
                    for lease in leases
                ]
                print("\nActive Leases:")
                print(tabulate(table, headers=headers, tablefmt="grid"))

        elif choice == '4':
            leases = impl.list_lease_history()
            if not leases:
                print("No lease history available.")
            else:
                headers = ["Lease ID", "Customer ID", "Vehicle ID", "Start Date", "End Date", "Lease Type"]
                table = [
                    [lease.get_lease_id(), lease.get_customer_id(), lease.get_vehicle_id(),
                     lease.get_start_date(), lease.get_end_date(), lease.get_lease_type()]
                    for lease in leases
                ]
                print("\nLease History:")
                print(tabulate(table, headers=headers, tablefmt="grid"))

        elif choice == '5':
            try:
                customer_id = int(input("Enter Customer ID: "))
                result = impl.get_lease_count_by_customer(customer_id)
                if result:
                    headers = ["Customer ID", "First Name", "Last Name", "Lease Count"]
                    table = [[result[0], result[1], result[2], result[3]]]
                    print(tabulate(table, headers=headers, tablefmt="grid"))
                else:
                    print("Customer not found or no leases.")
            except Exception as e:
                print(f"Error fetching lease count: {e}")

        elif choice == '6':
            try:
                car_id = int(input("Enter Car ID: "))
                lease_info = impl.get_days_to_lease_end_by_car_id(car_id)
                if lease_info is not None:
                    days_left, start_date, end_date, car = lease_info
                    headers = ["Car ID", "Make", "Model", "Lease Start Date", "Lease End Date", "Days Remaining"]
                    table = [[
                        car.get_vehicle_id(),
                        car.get_make(),
                        car.get_model(),
                        start_date.strftime("%Y-%m-%d"),
                        end_date.strftime("%Y-%m-%d"),
                        days_left
                    ]]
                    print("\nLease Details:")
                    print(tabulate(table, headers=headers, tablefmt="grid"))
                else:
                    print("No active lease found for this car.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            try:
                vid = int(input("Enter Car ID: "))
                start = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
                end = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
                lease_type = input("Enter lease type (daily/monthly): ").lower()

                cost = impl.calculate_lease_cost(vid, start, end, lease_type)
                print(f"Total lease cost: ${cost:.2f}")
            except Exception as e:
                print(f"Error calculating lease cost: {e}")

        elif choice == '8':
            customers = impl.get_customers_with_lease_counts()
            if not customers:
                print("No customers found.")
            else:
                headers = ["Customer ID", "First Name", "Last Name", "Number of Leases"]
                table = [[cust_id, first, last, count] for cust_id, first, last, count in customers]
                print(tabulate(table, headers=headers, tablefmt="grid"))

        elif choice == '9':
            break

        else:
            print("Invalid option. Try again.")


############################################################# Payment Management ###############################################
def payment_management_menu(impl):
    while True:
        print("\n--- Payment Management ---")
        print("1. Record Payment")
        print("2. Payment History")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                lease_id = int(input("Enter Lease ID: "))

                lease = impl.find_lease_by_id(lease_id)
                rental_amount = lease.get_rental_amount()

                print(f"Rental Amount to Pay: ${rental_amount:.2f}")
                amount = float(input("Enter payment amount: "))

                if amount != rental_amount:
                    print("Payment amount must match the rental amount exactly. Payment not recorded.")
                else:
                    impl.record_payment(lease_id, amount)
                    print("Payment recorded successfully.")

            except LeaseNotFoundException as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '2':
            try:
                customer_id = int(input("Enter Customer ID to fetch payment history: "))
                payments = impl.get_payment_history_by_customer_id(customer_id)

                if not payments:
                    print("No payments found for this customer.")
                else:
                    headers = ["Payment ID", "Lease ID", "Amount", "Date"]
                    print("\nPayment History:")
                    print(tabulate(payments, headers=headers, tablefmt="grid"))

            except ValueError:
                print("Invalid customer ID.")
            except Exception as e:
                print(f"Error fetching payment history: {e}")

        elif choice == '3':
            break

        else:
            print("Invalid option. Try again.")




def main():
    impl = ICarLeaseRepositoryImpl()

    while True:
        print("\n=== Car Rental Management System ===")
        print("1. Car Management")
        print("2. Customer Management")
        print("3. Lease Management")
        print("4. Payment Management")
        print("5. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == '1':
                car_management_menu(impl)
            elif choice == '2':
                customer_management_menu(impl)
            elif choice == '3':
                lease_management_menu(impl)
            elif choice == '4':
                payment_management_menu(impl)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")
        except (CarNotFoundException, CustomerNotFoundException, LeaseNotFoundException) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()