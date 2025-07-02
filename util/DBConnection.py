from util.PropertyUtil import PropertyUtil
import mysql.connector

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                config = PropertyUtil.get_property_dict()
                DBConnection.connection = mysql.connector.connect(**config)
                print("Database connection established.")
            except Exception as e:
                print(f"Failed to connect to database: {e}")
                raise
        return DBConnection.connection
