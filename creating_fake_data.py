from faker import Faker
import sqlite3

# Initialize Faker
fake = Faker('pt_BR')

# Connect to the database (SQLite in this example)
conn = sqlite3.connect('fake_database.db')
cursor = conn.cursor()

# Create a users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        address TEXT
    )
''')

# Create an orders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        quantity INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Generate and insert fake data into the users table
for i in range(5):
    name = fake.name()
    email = fake.email()
    address = fake.address()

    cursor.execute('INSERT INTO users (name, email, address) VALUES (?, ?, ?)', (name, email, address))

# Generate and insert fake data into the orders table
for user_id in range(1, 6):
    product = fake.word()
    quantity = fake.random_int(min=1, max=10)

    cursor.execute('INSERT INTO orders (user_id, product, quantity) VALUES (?, ?, ?)', (user_id, product, quantity))

# Commit to save the changes to the database
conn.commit()

# Close the connection
conn.close()