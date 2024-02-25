import pandas as pd
import numpy as np

np.random.seed(2)
data = {}
for i in range(20):
    data['col'+str(i)] = np.random.rand(200)

df = pd.DataFrame(data)

# Add some missing values
for i in range(20):
    df.iloc[np.random.randint(0, 200, 20), i] = np.NAN

# Introduce correlation
corr = 0.5
df['col0'] = df['col0'] + corr * df['col1']

# Shuffle the DataFrame
df = df.sample(frac=1).reset_index(drop=True)

print(df.head())

df.to_csv(f"C:/Users/mkrti/OneDrive/Документы/Python projects/Pandas/Data for pandas/pandas_practice.csv", index = False, mode='a')