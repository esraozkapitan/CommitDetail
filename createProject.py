import sqlite3
import datetime
class Checking(object):
    def __init__(self):
        self.conn = None

    def connectDb(self):
        try:
            self.conn = sqlite3.connect("D:/Projects/First/database.db")
        except Exception as e:
            print(f"Error connecting to db: {e}")
        return self.conn
    def check(self):
        self.connectDb()
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "SELECT INSERT_ON FROM PROJECT WHERE PROJECT_NAME = 'Web'")
            lastDate = cursor.fetchone()
            print(lastDate[0])
            dbTime = datetime.datetime(2024, 5, 30, 14, 55, 17, 440000)
            print(dbTime)

        except Exception as e:
            print(f"Error: {e}")
        self.conn.close()

if __name__ == "__main__":
    c = Checking()
    c.check()

