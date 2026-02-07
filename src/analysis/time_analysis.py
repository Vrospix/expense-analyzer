def monthly_spending(df):
    monthly = df.groupby(df['dates'].dt.to_period('M'))['amount'].sum()
    monthly.index = monthly.index.to_timestamp()
    return monthly