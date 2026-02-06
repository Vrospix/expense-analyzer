import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="expense-analyzer",
        user="expense_user",
        password="Minimum2710",
        host="localhost",
        port="5432"
        )
