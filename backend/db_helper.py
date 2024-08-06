# db_helper.py

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from mysql.connector import Error
from decimal import Decimal
load_dotenv()
global cnx

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Connect to the database

cnx = mysql.connector.connect(  
  host=db_host,
  user=db_user,
  password=db_password,
  database=db_name
)


def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()

        # Calling the stored procedure
        #cursor.callproc('insert_order_item', (food_item, quantity, order_id))
        query = "SELECT item_id, price FROM food_items WHERE name = %s"
        cursor.execute(query, (food_item,))
        result = cursor.fetchone()
        
        if not result:
            return False
        item_id, price = result
        price = Decimal(str(price))
        quantity = int(quantity)
        total_price = price * quantity
        query = "INSERT INTO orders ( order_id,item_id,total_price ,quantity) VALUES (%s, %s, %s,%s)"
        cursor.execute(query, (order_id,item_id,total_price ,quantity))
        
    
        # Committing the changes
        cnx.commit()

        # Closing the cursor
        cursor.close()

        print("Order item inserted successfully!")

        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if necessary
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()

        return -1

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    # Inserting the record into the order_tracking table
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    # Committing the changes
    cnx.commit()

    # Closing the cursor
    cursor.close()

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to get the total order price
    query = "SELECT SUM(total_price) FROM orders WHERE order_id = %s"
    cursor.execute(query, (order_id,))
    result = cursor.fetchone()
    cursor.close()
    return Decimal(str(result[0])) if result and result[0] is not None else Decimal('0')

    # Closing the cursor
    

   

# Function to get the next available order_id
def get_next_order_id():
    cursor = cnx.cursor()

    # Executing the SQL query to get the next available order_id
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None


if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    # insert_order_tracking(99, "in progress")
    print(get_next_order_id())
