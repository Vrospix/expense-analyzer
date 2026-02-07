import pandas as pd
from db.connection import get_connection
from analysis.cleaning import clean_expenses
from analysis.summary import category_summary
from analysis.visualization import plot_category_summary
from analysis.visualization import plot_monthly_trend
from analysis.time_analysis import monthly_spending
from analysis.anomaly import detect_anomalies
from analysis.forecast import prepare_ml_data, train_and_predict

def main() -> pd.DataFrame:
    conn = get_connection()
    query = "SELECT * FROM expense;"
    df = pd.read_sql(query, conn)
    conn.close()
    
    clean_df = clean_expenses(df)
    clean_df.to_csv("output/data.csv", index=False)
    print("Data saved to data.csv succesfully!")
    
    return clean_df

def summary():
    clean_df = main()
    summary = category_summary(clean_df)
    plot_category_summary(summary)
    return summary


def monthly():
    clean_df = main()
    monthly = monthly_spending(clean_df)
    return monthly


def anomalies():
    anomalies = detect_anomalies(monthly())
    return anomalies

def predict():
    ml_df = prepare_ml_data(monthly())
    prediction, model = train_and_predict(ml_df)

def run_pipeline():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM expense", conn)
    conn.close()

    clean_df = clean_expenses(df)
    monthly = monthly_spending(clean_df)
    anomalies = detect_anomalies(monthly)

    ml_df = prepare_ml_data(monthly)
    prediction, _ = train_and_predict(ml_df)

    return {
        "clean_df": clean_df,
        "monthly": monthly,
        "anomalies": anomalies,
        "forecast": prediction
    }

if __name__ == "__main__":
    run_pipeline()