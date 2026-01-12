import pandas as pd

df = pd.read_csv("data.csv", encoding="latin1")
# df = pd.read_excel("Book1.xlsx")
# df = pd.read_excel("SampleSuperstore.xlsx")
# df = pd.read_json("sample_Data.json")
print(df)

