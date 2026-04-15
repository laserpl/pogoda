import requests
import pandas as pd

def wszystkie_kraje():
    url = "https://restcountries.com/v3.1/all?fields=name,flags,population,subregion,independent"
    odpowiedz = requests.get(url)
    dane = odpowiedz.json()

    kraje = []
    for x in dane:
        nowy = {
            "nazwa": x.get("name").get("common"),
            "oficjalna_nazwa": x.get("name").get("official"),
            "flaga": x.get("flags").get("png"),
            "populacja": x.get("population"),
            "niepodleglosc": x.get("independent"),
            "region": x.get("subregion"),

        }
        kraje.append(nowy)

    return kraje


result = wszystkie_kraje()

df = pd.DataFrame(result)
df.to_excel("kraje.xlsx", index=False)

df = pd.read_excel("kraje.xlsx")

a = df.head(3)
b = df.tail(3)

# df.info()

c = df.describe()

d = list(df.columns)

# pd.set_option("display.max_columns", None)
# pd.set_option('display.max_rows', None)
# SORTOWANIE
# e = df.sort_values("populacja", ascending=False)
# print(e[["nazwa","populacja"]])
f = df.sort_values("nazwa")
# print(f)

# FILTROWANIE
g = df[ df["populacja"] > 500_000_000 ]
h = df[ df["region"] == "Eastern Asia" ]
i = df[ (df["region"] == "Eastern Asia") & (df["populacja"] > 100_000_000) ]
j = df[ (df["region"] == "Eastern Europe") | (df["region"] == "Eastern Asia") ]

k = df["region"].value_counts()
l = df["niepodleglosc"].value_counts()

# GRUPOWANIE
n = df.sort_values("populacja", ascending=True)
m = n.groupby("region")["populacja"].mean() # TODO

df["populacja_mln"] = round(df["populacja"] / 1_000_000)

o = df.groupby("region")["populacja_mln"].mean()

df = df.dropna()
print(df)
