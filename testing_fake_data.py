import unittest
import sqlite3

class TestDatabaseOperations(unittest.TestCase):
    def test_inner_join(self):
        # Connect to the database
        conn = sqlite3.connect('fake_database.db')
        cursor = conn.cursor()

        # Execute an INNER JOIN to retrieve data from users and orders
        cursor.execute('''
            SELECT users.id, users.name, orders.product, orders.quantity
            FROM users
            INNER JOIN orders ON users.id = orders.user_id
        ''')

        # Get the results
        results = cursor.fetchall()

        # Check if there is at least one result
        self.assertTrue(len(results) > 0)

        # Print the results
        print("INNER JOIN Result:")
        for result in results:
            print(result)

        # Close the connection
        conn.close()

if __name__ == '__main__':
    unittest.main()
