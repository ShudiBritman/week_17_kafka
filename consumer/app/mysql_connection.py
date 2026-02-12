import mysql.connector
import os
import time

config = {
    'user': os.getenv('SQL_USER', 'root'),
    'host': os.getenv('SQL_HOST', 'localhost'),
    'port': int(os.getenv('SQL_PORT', 3306)),
    'password': os.getenv('SQL_PASSWORD')
}

class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)

            max_retries = 10
            delay = 3

            for attempt in range(1, max_retries + 1):
                try:
                    cls._instance.connection = mysql.connector.connect(**config)
                    break
                except Exception as e:
                    time.sleep(delay)

        return cls._instance

    def get_connection(self):
        return self.connection
