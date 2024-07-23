import time

from crazy import *
dataframe_completely_display()
pro = ts.pro_api('ad047441cc72120d3197505b58f84964148b449405d5e67b410a8bac')
df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
df = df[df['delist_date'].isna()]  # 删掉已经退市的转债
df = df[df['remain_size'] != 0]  # 删掉剩余规模为0的转债
df = df[~df['list_date'].isna()]  # 删掉还没有可以上市交易的转债
dict1 = dict(zip(df['ts_code'],df['stk_code']))
print(dict1)
from xtquant import xtdata
#获取可转债基础信息列表
df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date")
for i ,ii in tqdm(dict1.items()):
    code = ii
    period = '1m'
    day = '20240722'
    day1 = '20240722'
    xtdata.download_history_data(stock_code=code, period=period, start_time=day, end_time=day1)
    time.sleep(0.1)