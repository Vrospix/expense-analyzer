import pandas as pd
from db.connection import get_connection
from analysis.cleaning import clean_expenses
from analysis.summary import category_summary
from analysis.visualization import plot_category_summary
from analysis.visualization import plot_monthly_trend
from analysis.time_analysis import monthly_spending
from analysis.anomaly import detect_anomalies

def main():
    conn = get_connection()
    query = "SELECT * FROM expense;"
    df = pd.read_sql(query, conn)
    clean_df = clean_expenses(df)
    clean_df.to_csv("output/data.csv", index=False)
    print("Data saved to data.csv succesfully!")
    summary = category_summary(clean_df)
    print(category_summary(clean_df))
    plot_category_summary(summary)
    monthly = monthly_spending(clean_df)
    plot_monthly_trend(monthly)
    anomalies = detect_anomalies(monthly)
    print("Unusual spending months:")
    print(anomalies)
    conn.close()

if __name__ == "__main__":
    main()
