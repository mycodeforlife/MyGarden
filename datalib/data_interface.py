# from flask_mysqldb import MySQL
import pymysql
import json

class dataInterface:

    connection = pymysql.connect(host="localhost", user="root", passwd="art@6085", db="mygarden")

    def __init__(self):
        self.connection = pymysql.connect(host="localhost", user="root", passwd="art@6085", db="mygarden")

    def get_garden_tools(self):
        get_query = "SELECT * FROM gardentools;"
        db_cursor = self.connection.cursor()
        db_cursor.execute(get_query)
        desc = db_cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in db_cursor.fetchall()]
        return data

    def get_garden_calender(self):
        pass

    def get_recent_posts(self, max_number):
        pass


class dataConverter:

    def __init__(self):
        pass

    def convert_to_json(self):
        pass

    def convert_to_sql_query(self):
        pass



