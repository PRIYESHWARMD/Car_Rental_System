
# Car Rental System

The **Car Rental System** is a terminal-based Python application designed to manage the operations of a car rental agency. It enables users to handle vehicles, customers, leases, and payments through a user-friendly menu interface with MySQL database integration.

---

## Project Overview

This system streamlines operations for rental businesses by:

* Managing customer details
* Tracking vehicle availability
* Creating leases (daily/monthly)
* Recording payments
* Generating reports and summaries

---

## Technologies Used

* Python 3
* MySQL
* MySQL Connector (`mysql-connector-python`)
* Object-Oriented Programming (OOP)
* Custom Exception Handling
* PyCharm IDE (recommended)

---

## Design Principles Followed

* **Modular Design** – Organized into packages (`dao`, `model`, `util`, etc.)
* **OOP Concepts** – Uses classes with encapsulation, abstraction, inheritance
* **Interface Pattern** – Implements an interface-like pattern (`ICarLeaseRepository`)
* **Exception Handling** – Robust use of custom exceptions

---

## Features

### Vehicle Management

* Add, remove, or search vehicles
* List available cars
* Count leases per vehicle

### Customer Management

* Add customers with validation
* Update, delete, and search by ID
* View all registered customers

### Lease Management

* Create new leases (daily/monthly)
* Search leases by date range
* View lease history
* Count leases per customer
* Calculate lease costs
* Show remaining lease days

### Payment Handling

* Record lease payments
* View payment history
* Show total revenue

---

## Input Validations

* Email must include `@` and end with `.com`
* Phone number must be exactly 10 digits
* First and last names must contain only letters

---

## Error Handling

| Exception                   | Description                       |
| --------------------------- | --------------------------------- |
| `CarNotFoundException`      | Raised if a car ID does not exist |
| `CustomerNotFoundException` | Raised for invalid customer ID    |
| `LeaseNotFoundException`    | Raised when lease ID is not found |

---

## Testing

* Basic unit tests included in the `test/` package
* Tests include:

  * Vehicle creation
  * Lease counting
  * Exception scenarios

---

## Database Schema Overview

| Table      | Purpose                                            |
| ---------- | -------------------------------------------------- |
| `vehicle`  | Stores vehicle details (make, model, rate, etc.)   |
| `customer` | Holds customer information                         |
| `lease`    | Contains lease records (dates, type, car ID, etc.) |
| `payment`  | Records payment history linked to leases           |

---

## How to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/car-rental-system.git
   cd car-rental-system
   ```

2. **Set up MySQL database**

   * Create a database named `carlease`
   * Create tables: `vehicle`, `customer`, `lease`, `payment`
   * (Optional) Use SQL script from the `db/` folder if available

3. **Configure database connection**

   * Update `config/db.properties` with your database credentials:

     ```
     host=localhost
     port=3306
     dbname=carlease
     user=root
     password=yourpassword
     ```

4. **Install required Python packages**

   ```bash
   pip install mysql-connector-python
   ```

5. **Run the main application**

   ```bash
   python main/main.py
   ```

