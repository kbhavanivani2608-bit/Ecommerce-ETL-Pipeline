import pandas as pd
import mysql.connector

# EXTRACT
df = pd.read_csv("data/orders.csv")

print("===== RAW DATA =====")
print(df)

# TRANSFORM
df = df.drop_duplicates()

print("\n===== AFTER REMOVING DUPLICATES =====")
print(df)

# LOAD
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345bhanu",
    database="ecommerce_etl"
)

print("\nMYSQL CONNECTION SUCCESS")

cursor = connection.cursor()

insert_query = """
INSERT INTO orders
(order_id, customer_id, product, category, quantity, price, order_date)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

connection.commit()

print("\n===== LOAD SUCCESSFUL =====")
print(f"{len(df)} records loaded into MySQL.")

cursor.close()
connection.close()
