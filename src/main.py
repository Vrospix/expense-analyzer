import pandas as pd
from db.connection import get_connection

def main():
    conn = get_connection()
    query = "SELECT * FROM expense;"
    df = pd.read_sql(query, conn)
    df.to_csv("src/db/data.csv", index=False)
    print("Data saved to data.csv succesfully!")
    print(df)
    conn.close()

if __name__ == "__main__":
    main()
