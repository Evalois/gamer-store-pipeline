# Simple synthetic trainer example for demand forecasting prototype
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from joblib import dump
from pathlib import Path

def generate_sample_series(days=180):
    idx = pd.date_range(end=pd.Timestamp.today(), periods=days)
    # synthetic daily demand with weekly seasonality + noise
    data = (20 + 5*np.sin(2*np.pi*idx.dayofweek/7) + np.random.poisson(2, size=len(idx))).astype(int)
    return pd.DataFrame({'date': idx, 'sales_qty': data})

def featurize(df):
    df = df.set_index('date').asfreq('D').fillna(0)
    df['lag_1'] = df['sales_qty'].shift(1).fillna(0)
    df['lag_7'] = df['sales_qty'].shift(7).fillna(0)
    df['dow'] = df.index.dayofweek
    df = df.dropna()
    X = df[['lag_1','lag_7','dow']]
    y = df['sales_qty']
    return X, y

def train_and_save(path='ml_models/rf_demand.joblib'):
    df = generate_sample_series()
    X, y = featurize(df)
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    dump(model, path)
    print('Model saved to', path)

if __name__ == '__main__':
    train_and_save()
