from fastapi import APIRouter
from joblib import load
import pandas as pd
from datetime import datetime, timedelta
router = APIRouter()

@router.get('/predict/{sku}')
def predict(sku: str):
    # Loads a toy model stored in ml_models/rf_demand.joblib and predicts next 7 days using naive features.
    try:
        model = load('/app/ml_models/rf_demand.joblib')
    except Exception as e:
        return {'error': 'model not found, run ml/train.py to create a model'}
    today = pd.Timestamp.today().normalize()
    preds = []
    # We'll create simple features based on zeros (for demo only)
    for i in range(1,8):
        date = today + pd.Timedelta(days=i)
        # dummy lags
        X = [[0,0,date.dayofweek]]
        pred = model.predict(X)[0]
        preds.append({'date': str(date.date()), 'predicted_qty': float(pred)})
    return {'sku': sku, 'predictions': preds}
