import pyupbit

access = "utJ2gTv0gqZfX4an5TTeUxUS1Y4y2GCP4BvkxfQ2"          # 본인 값으로 변경
secret = "82ypo3SsOYChqnKPaxGoU6JnFPLBngXbSp7lCCFF"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-STEEM"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회