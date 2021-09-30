import psycopg2


class DBConnection:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print('inside __new__')
            cls.instance = super().__new__(DBConnection)
            return cls.instance
        return cls.instance

    def __init__(self, db_name='MoviesDB'):
        self.name = db_name
        print('inside init')
        # connect takes url, dbname, user-id, password
        self.conn = self.connect(db_name)
        self.cursor = self.conn.cursor()

    def connect(self, name):
        try:
            return psycopg2.connect(database=self.name, user='postgres', password='root', host='127.0.0.1', port='5432')
        except psycopg2.Error as e:
            pass

    def createTables(self):
        print('in create tb')
        if self.conn:
            # print('in conn')
            cursor = self.conn.cursor()
            sqlstr = open("db_tables/revenue_analyser.sql")
            sql_as_string = sqlstr.read()
            print(sql_as_string)
            cursor.execute(sql_as_string)

    def verifyConnection(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("select version()")
            data = cursor.fetchone()
            print("Connection established to: ", data)
            if data:
                return True
            else:
                return False

    def __del__(self):
        self.cursor.close()
        self.conn.close()
