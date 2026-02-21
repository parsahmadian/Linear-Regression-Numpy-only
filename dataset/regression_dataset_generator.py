import numpy as np
import pandas as pd

file_name = "house_price_1000.csv"
np.random.seed(42)
n = 1000

# generate feature data
area = np.random.normal(loc=120, scale=30, size=n).clip(40, 300)
rooms = (area / 30).astype(int).clip(1, 6)
age = np.random.randint(0, 40, n)
distance = np.random.normal(loc=8, scale=4, size=n).clip(0.5, 30)

# generate labels
price = (
    area * 8
    + rooms * 150
    - age * 20
    - distance * 30
    + np.random.normal(0, 200, n)
)

# convert array to dataframe
df = pd.DataFrame({
    "Area": area.astype(np.int64),
    "Rooms": rooms,
    "BuildingAge": age,
    "DistanceToCenter": distance.round(1),
    "Price": price.astype(np.int64)
})

df.to_csv(file_name, index=False)
print(f"{file_name} Saved✅")