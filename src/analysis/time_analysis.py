def monthly_spending(df):
    monthly = df.groupby(df['dates'].dt.to_period('M'))['amount'].sum()
    return monthly