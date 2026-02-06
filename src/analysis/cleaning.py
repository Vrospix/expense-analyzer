import pandas as pd

def clean_expenses(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['dates'] = pd.to_datetime(df['dates'], errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    df = df.dropna(subset=['dates', 'amount', 'category'])

    df = df[df['amount'] > 0]

    df['category'] = df['category'].str.strip().str.title()

    return df
