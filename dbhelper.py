import sqlite3

class DBHelper:
    #Initialize
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    #Create table
    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS uniqueuser (description text)"
        self.conn.execute(stmt)
        self.conn.commit()

    #Add new chatid
    def add_user(self, user_id):
        stmt = "INSERT INTO uniqueuser (description) VALUES (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    #TBC
    def delete_user(self, user_id):
        stmt = "DELETE FROM uniqueuser WHERE description = (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    #Retrieve prevlocation
    def get_user(self):
        stmt = "SELECT description FROM uniqueuser"
        return [x[0] for x in self.conn.execute(stmt)]