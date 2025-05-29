import pandas as pd

df = pd.read_csv("./weather.csv")

print(f"INFO: {df.info()}")
print(f"SUM NULL: \n{df.isnull().sum()}")

# As there are not many null rows we remove them
df = df.dropna()

print(f"SUM NULL AFTER REMOVE: \n{df.isnull().sum()}")

# New column for temperature variation
df["temp_diff"] = df["MaxTemp"] - df["MinTemp"]
print(df.head())
print("\n\n\n")

# Change dataType
df["Rainfall"] = df["Rainfall"].astype("int64")
print(f"{df["Rainfall"].info()}")

# Export to csv
df.to_csv("./weather_after_changes.csv", index=False, header=True, sep=",", decimal=".")