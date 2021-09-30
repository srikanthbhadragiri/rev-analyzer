import ClsDBConn


class Data(ClsDBConn.DBConnection):
    def __init__(self):
        print("sub class")
        print(self.verifyConnection())