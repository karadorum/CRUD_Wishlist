import MySQLdb as mdb


class Database():
    def __init__(self):
        try:
            self.conn = mdb.connect(
            host='127.0.0.1',
            user='root',
            password='111111',
            db='wishlist',
            port=3306)
            self.cursor = self.conn.cursor()

        except mdb.Error as e:
            print(e)

    def connect(self):
        return self.conn

    def cursor(self):
        return self.cursor

    def commit(self):
        self.conn.commit()

    def disconnect_db(self):
        """ commit changes to database and close connection """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def show_data(self):
        self.cursor.execute("SELECT * FROM wishes")
        response = self.cursor.fetchall()
        return response

    def insert_data(self, wish, desc, url):
        self.cursor.execute(
        'INSERT INTO wishes (wish, description, url) VALUES ("{}", "{}", "{}");'.format(wish, desc, url))
        self.commit()

    def delete_row(self, wish, desc, url):
        self.cursor.execute(
        'DELETE FROM wishes WHERE wish="{}" AND description="{}" AND url="{}";'.format(
        wish, desc, url))
        self.commit()

    def change_data(self, wish, description, url, new_wish, new_desc, new_url):
        self.cursor.execute(
        'UPDATE wishes SET wish = "{}", description = "{}", url = "{}" WHERE wish = "{}" AND description = "{}" AND url = "{}";'.format(
            new_wish, new_desc, new_url, wish, description, url))
        self.commit()
