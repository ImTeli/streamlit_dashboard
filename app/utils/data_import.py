import json
import pandas as pd

def generate_df():
    with open("app/data/vendas.json") as file:
        data = json.load(file)
    df = pd.DataFrame.from_dict(data)
    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], format="%d/%m/%Y")
    return df