import pandas as pd
from same_same.data_loader import load_data

def test_load_data(tmp_path):
    df_data = pd.DataFrame({"Description": ["Defect 1", "Defect 2"]})
    csv_path = tmp_path / "test.csv"
    df_data.to_csv(csv_path, index=False)
    
    df = load_data(str(csv_path))
    assert len(df) == 2
    assert df.iloc[0]["Description"] == "Defect 1"
