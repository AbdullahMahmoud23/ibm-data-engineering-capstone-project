# Import libraries required for connecting to mysql
import mysql.connector
# Import libraries required for connecting to PostgreSql
import psycopg2

# Connect to MySQL
mysql_conn = mysql.connector.connect(
    user='root',
    password='asdfg123@.com',
    host='localhost',
    database='sales'
)
# Connect to PostgreSql
pg_conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='1344',
	host='localhost',
	port= "5433"
)
# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
	cursor = pg_conn.cursor()
	# Query the maximum rowid currently in the warehouse
	cursor.execute("SELECT MAX(rowid) FROM sales_data;")
	result = cursor.fetchone()[0]
	cursor.close()

	# If the table is completely empty, return 0 so it pulls everything
	if result is None:
		return 0
	return result

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
	cursor = mysql_conn.cursor()
    # Select only the rows that are newer than our last_row_id
	cursor.execute("SELECT * FROM sales_data WHERE rowid > %s;", (rowid,))
	records = cursor.fetchall()
	cursor.close()
	return records

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in PostgreSql.

# Task 3 - Insert the additional records from MySQL into PostgreSql data warehouse
def insert_records(records):
    # If there are no new records, do nothing
    if not records:
        return
        
    cursor = pg_conn.cursor()
    
    # Updated query: Only inserting the 4 columns that actually exist in MySQL
    insert_query = """
    INSERT INTO sales_data (rowid, product_id, customer_id, quantity) 
    VALUES (%s, %s, %s, %s);
    """
    
    # executemany is highly optimized for bulk inserts
    cursor.executemany(insert_query, records)
    pg_conn.commit()
    cursor.close()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
mysql_conn.close()
# disconnect from DB2 or PostgreSql data warehouse 
pg_conn.close()

print("ETL Sync Complete. Connections closed.")
# End of program