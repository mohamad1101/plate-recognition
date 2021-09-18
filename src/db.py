import pyodbc
import logging
from parameters import db_path, db_pass
import datetime
from imp import reload
import os


def connect():
    ConFileName = (r'c:\\Users\\mohamad\\Desktop\\plate\\plate-recognition-main\\src\\db\\iCCard.mdb')
    # conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\Users\mohamad\Desktop\plate\plate-recognition-main\src\db\iCCard.mdb;')
    # cursor = conn.cursor()
    driver = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    pyodbc.pooling = False
    conn = pyodbc.connect(r"{}DBQ={}; PWD={};".format(driver, db_path, db_pass))
    cursor = conn.cursor()
    return cursor, conn


class DB:

    def __init__(self):
        pass

    def select_rows(self, cursor, conn, query):
        rows = []
        cursor.execute(query)
        for row in cursor.fetchall():
            rows.append(row)
        return rows

    def list_of_tables(self, cursor, conn):
        for row in cursor.tables():
            print(row.table_name)

    def query_running(func):
        def run(self, cursor, conn, query, *args):
            func(self, cursor, conn, query, *args)
            conn.commit()
            logging.info("Query {} run with args {}".format(query, args))

        return run

    @query_running
    def create_table(self, cursor, conn, query):
        cursor.execute(query)

    @query_running
    def remove_table(self, cursor, conn, query):
        cursor.execute(query)

    @query_running
    def insert(self, cursor, conn, query, values):
        cursor.execute(query, values)

    @query_running
    def update(self, cursor, conn, query, values):
        cursor.execute(query, values)


if __name__ == "__main__":
    reload(logging)
    logging.basicConfig(handlers=[logging.FileHandler(
        filename=os.path.join('logs', 'logs.log'),
        encoding='utf-8', mode='a+'
    )
    ],
        format='%(asctime)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO)

    db = DB()
    cursor, conn = connect()

    # query = "INSERT INTO Plate_table ([image_path], [plate_text],[capture_date]) VALUES (?,?, ?)"
    # values = ("val", "text plate", datetime.datetime.now())
    # db.insert(cursor, conn, query, values)

    # query = "UPDATE Plate_table SET plate_text = ? WHERE capture_date = ?"
    # values = ("update value", datetime.datetime(2021, 6, 11, 19, 52, 37))
    # db.update(cursor, conn, query, values)

    query = 'select * from {}'.format("Plate_table")

    print(db.select_rows(cursor, conn, query))
    print(len(db.select_rows(cursor, conn, query)))
    querySelect = 'select * from plate_text'.format("Plate_table")
    print(querySelect + "-------")
    # query = 'DROP TABLE Plate_table'
    # db.remove_table(cursor, conn, query)

    # query = "CREATE TABLE Plate_table(image_path varchar(70), plate_text varchar(70), capture_date date)"
    # db.create_table(cursor, conn, query)

    # print(db.list_of_tables(cursor, conn))
