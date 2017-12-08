import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset='utf8'
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Client:
    def __init__(self, db_connection, login):
        self.db_connection = db_connection.connection
        self.login = login
        self.client_info = None

    def select(self):
        c = self.db_connection.cursor()
        c.execute('SELECT * FROM main_app_client WHERE login = %s;', [self.login])
        self.client_info = c.fetchone()
        c.close()
        print(self.client_info)

user = 'FlowerLight_admin'
password = 'admin'
db = 'FlowerLight_db'
conn = Connection(user, password, db)

with conn:
    client = Client(conn, 'elizarov')
    client.select()

