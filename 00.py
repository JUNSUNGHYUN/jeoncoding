import pyupbit

df = pyupbit.get_ohlcv("KRW-STEEM","day",200)
# print(df.head())
df.to_excel("steem.xlsx")