import csv

import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="firstdb"
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Define the SQL query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS weather_data (
    city VARCHAR(255),
    date DATE,
    temperature FLOAT,
    humidity FLOAT,
    rainfall FLOAT,
    wind_speed FLOAT
);

"""

# Execute the create table query
cursor.execute(create_table_query)
#cursor.commit()
# Load the dataset from CSV
csv_file = "D:\\io (data)\\weather_cleaned.csv"

with open(csv_file, "r") as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip the header row

    insert_query = "INSERT INTO weather_data (city, date, temperature, humidity, rainfall, wind_speed) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, csv_data)

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()