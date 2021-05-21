import sqlite3

class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS uniqueuser (description text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_user(self, user_id):
        stmt = "INSERT INTO uniqueuser (description) VALUES (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_user(self, user_id):
        stmt = "DELETE FROM uniqueuser WHERE description = (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_user(self):
        stmt = "SELECT description FROM uniqueuser"
        return [x[0] for x in self.conn.execute(stmt)]