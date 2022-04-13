import psycopg2


def safe_call(func_to_decorator):
    def wrapper(self, data):
        try:
            return func_to_decorator(self, data)
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL:", _ex)

    return wrapper


class Datasource:

    def __init__(self, host, user, password, database):
        self.connection = self.get_connection({
            "host": host,
            "user": user,
            "password": password,
            "database": database
        })

    def __del__(self):
        self.close_connection()

    @safe_call
    def get_connection(self, data):
        return psycopg2.connect(
            host=data['host'],
            user=data['user'],
            password=data['password'],
            database=data['database']
        )

    @safe_call
    def execute(self, command):
        with self.connection.cursor() as cursor:
            cursor.execute(command)
            return cursor.fetchall()

    def get_education_quality_view(self):
        return self.execute('''SELECT * FROM education_quality_view''')

    def get_statement_view(self):
        return self.execute('''SELECT * FROM statement_view''')

    def close_connection(self):
        self.connection.close()
        print("[INFO] PostgreSQL connection close")
