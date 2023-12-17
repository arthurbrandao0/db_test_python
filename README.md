# Fake Database with Faker in Python

This project demonstrates how to use the `Faker` library in Python to generate fake data and create a simple SQLite database with two tables (`users` and `orders`). Additionally, it includes a test case that utilizes an `INNER JOIN` to retrieve related data from both tables.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/arthurbrandao0/db_test_python.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd db_test_python
    ```

3. **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
   ```
   
6. **Run the script to create the fake database:**

    ```bash
    python create_fake_database.py
    ```
   
 Database Structure
------------------

The script creates two tables in an SQLite database:

1.  **users:**
    
    *   id (Primary Key)
    *   name
    *   email
    *   address
2.  **orders:**
    
    *   id (Primary Key)
    *   user\_id (Foreign Key referencing users.id)
    *   product
    *   quantity
    
Usage
-----

### Test INNER JOIN

The included test case (`TestDatabaseOperations.test_inner_join`) performs an `INNER JOIN` operation between the `users` and `orders` tables to retrieve related data.

To run the test:

```bash
python test_database_operations.py
```

The test checks if there is at least one result and prints the INNER JOIN result.
