import pandas as pd
from db.connection import get_connection
from analysis.cleaning import clean_expenses
from analysis.summary import category_summary

def main():
    conn = get_connection()
    query = "SELECT * FROM expense;"
    df = pd.read_sql(query, conn)
    clean_df = clean_expenses(df)
    clean_df.to_csv("output/data.csv", index=False)
    print("Data saved to data.csv succesfully!")
    print(clean_df[['category', 'amount']])
    print(category_summary(clean_df))
    conn.close()

if __name__ == "__main__":
    main()
