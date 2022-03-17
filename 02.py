import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret)
# resp = upbit.buy_market_order("KRW-OMG",10000)
# pprint.pprint(resp)

omg_balance = upbit.get_balance("KRW-OMG")
print(omg_balance)
# upbit.shell_market_order("KRW-OMG",10000)
