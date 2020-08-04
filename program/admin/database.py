#-*-coding:utf-8 -*
"""Database module.
"""
import requests
import mysql.connector

from program.admin.config import HOST, USER, PASSWORD, DATABASE_NAME,\
HEADER

class Database:
    """Database class.
    """
    def __init__(self):
        self.engine = None
        self.categories = None
        self.connection = mysql.connector.connect\
        (host=HOST, user=USER, password=PASSWORD)
        self.cursor = None
        self.status = False
        self.source = {}

    def reset(self, engine):
        """Method that resets the database (i.e. drop, create and use DB).
        """
        self.engine = engine
        self.categories = engine.categories
        self.execute_one(self.delete())
        self.execute_one(self.create())
        self.execute_one(self.use())
        self.categories.reset(self.engine)

    def verify(self, parameters):
        """Method that verify the truth of a given sql statement (provided
        by various modules methods) and returns a boolean.
        """
        self.open_cursor()
        self.cursor.execute(parameters[0])
        self.cursor.fetchall()
        if self.cursor.rowcount >= 1:
            self.status = True
        else:
            self.status = False
        self.close_cursor()
        return self.status

    @classmethod
    def exists(cls):
        """Method that provides the sql statement
        for DB existance verification.
        """
        statement = "SHOW DATABASES LIKE '%s'"% DATABASE_NAME
        message = "No DB"
        parameters = [statement, message]
        return parameters

    @classmethod
    def delete(cls):
        """Method that provides the sql statement for
        DB deletion.
        """
        statement = "DROP DATABASE IF EXISTS %s"% DATABASE_NAME
        parameters = [statement, None]
        return parameters

    @classmethod
    def create(cls):
        """Method that provides the sql statement for
        DB creation.
        """
        statement = "CREATE DATABASE IF NOT EXISTS %s CHARACTER\
        SET 'utf8';"% DATABASE_NAME
        parameters = [statement, None]
        return parameters

    def download(self, parameters):
        """Method that makes a parameterized (provided
        by categories and products modules methods) request to OFF API.
        """
        try:
            response_api = requests.get(parameters[0],\
            headers=HEADER, params=parameters[1])
            self.source = response_api.json()
        except requests.HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print("HTTP request to \"", parameters[0], "\" successfull")

        # response_api = requests.get(parameters[0],\
        # headers=HEADER, params=parameters[1])
        # self.source = response_api.json()
        # if not response_api:
        #     print ("An error occured. Please try later or contact APP owner")
        # else:
        #     print("HTTP request to \"", parameters[0], "\" successfull")

    @classmethod
    def use(cls):
        """Method that sets the appropriate database to use for
        the program.
        """
        statement = "USE %s"% DATABASE_NAME
        parameters = [statement, None]
        return parameters

    def open_cursor(self):
        """Method that open a connection cursor.
        """
        self.cursor = self.connection.cursor()

    def open_cursor_b(self):
        """Method that open a connection cursor.
        """
        self.cursor = self.connection.cursor(buffered=True)

    def close_cursor(self):
        """Method that close a connection cursor.
        """
        self.cursor.close()

    def execute_one(self, parameters):
        """Method that execute a sql statement (provided
        by various modules methods) once.
        """
        self.open_cursor()
        self.cursor.execute(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()

    def execute_many(self, parameters):
        """Method that execute a sql statement (provided
        by various modules methods) multiple times.
        """
        self.open_cursor()
        self.cursor.executemany(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()
