import pandas as pd

years = ['2010', '2011', '2012', '2013']
dfs = []
for year in years:
    df = pd.read_csv(f"../data/raw/RO_LFS_{year}_Y.csv", low_memory=False)
    df['YEAR'] = int(year)
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)
data.to_csv("../data/processed/data_concat.csv", encoding="utf-8", float_format="%.2f")


features = ['SEX', 'AGE', 'EDUCSTAT', 'DEGURBA', 'STAPRO', 'TEMP', 'FTPT', 'COURATT']
target = 'ILOSTAT'

data = data[features + [target]].copy()

data = data[data[target].notna()]
data[target] = (data[target] == 2).astype(int)


data.dropna(subset=features + [target], inplace=True)


data_encoded = pd.get_dummies(data, columns=features, drop_first=True)

data.to_csv("../data/processed/data_processed.csv", encoding="utf-8", float_format="%.2f")