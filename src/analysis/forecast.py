import pandas as pd
from sklearn.linear_model import LinearRegression

def prepare_ml_data(monthly):
    df = monthly.reset_index()
    df.columns = ['month', 'total']

    df['month_index'] = range(len(df))
    return df

def train_and_predict(df):
    X = df[['month_index']]
    y = df['total']

    model = LinearRegression()
    model.fit(X, y)

    next_month = [[df['month_index'].max() + 1]]
    prediction = model.predict(next_month)

    return prediction[0], model