import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="MoviesDB", user='postgres', password='root', host='127.0.0.1', port='5432'
)
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

# Retrieving data
cursor.execute('''SELECT * from movie_tbl''')

# Fetching 1st row from the table
result = cursor.fetchone();
print(result)

# Fetching 1st row from the table
result = cursor.fetchall();
print(result)

# Closing the connection
conn.close()
