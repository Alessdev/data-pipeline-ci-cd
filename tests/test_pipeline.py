import pandas as pd
from src.pipeline import transform_data

def test_total_calculation():
    df = pd.DataFrame({
         "price": [10, 20],
         "quantity": [2, 3]
    })
    result = transform_data(df)
    assert result["total"].tolist() == [20, 60]

