import psycopg2


def establishConn():
    return psycopg2.connect(
        database="MoviesDB", user='postgres', password='root', host='127.0.0.1', port='5432'
    )


# conn = establishConn()


def createTables(conn):
    # print('in create tb')
    if conn:
        # print('in conn')
        cursor = conn.cursor()
        sqlstr = open("db_tables/revenue_analyser.sql")
        sql_as_string = sqlstr.read()
        print(sql_as_string)
        cursor.execute(sql_as_string)


def verifyConnection(conn):
    if conn:
        cursor = conn.cursor()
        cursor.execute("select version()")
        data = cursor.fetchone()
        print("Connection established to: ", data)
        if data:
            return True
        else:
            return False




# createTables(conn)
# verifyConnection(conn)




# def retriveData(conn, table_name):
#     if conn:
#         cursor = conn.cursor()
#
#         cursor.execute("SELECT * FROM %s " % table_name)
#
#         # Fetching 1st row from the table
#         result = cursor.fetchall();
#         print(result)


# retriveData(conn, 'movie_tbl')

# def insertData(conn, table_name, values):
#     if conn:
#         cursor = conn.cursor()


# movie_info = {'title': 'Max 2', 'duration': 90, 'lang': 'English'}

# print(movie_info['duration'])
