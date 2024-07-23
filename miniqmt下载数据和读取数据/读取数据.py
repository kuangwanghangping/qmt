import time

from xtquant import xtdata
from crazy import *
dataframe_completely_display()
pro = ts.pro_api('ad047441cc72120d3197505b58f84964148b449405d5e67b410a8bac')
df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
df = df[df['delist_date'].isna()]  # 删掉已经退市的转债
df = df[df['remain_size'] != 0]  # 删掉剩余规模为0的转债
df = df[~df['list_date'].isna()]  # 删掉还没有可以上市交易的转债
dict1 = dict(zip(df['ts_code'],df['stk_code']))
print(dict1)
zhangfu_dict = {}
chengjiaoe_dict = {}
for i ,ii in tqdm(dict1.items()):
    code =[f'{ii}']
    period = '1m'
    day = '20240722'
    data_dir = r'G:\国金QMT交易端模拟\userdata_mini\datadir'
    kline_data = xtdata.get_local_data(field_list=[], stock_list=code, period=period, start_time=day,
                                       end_time=day, count=-1, data_dir=data_dir)
    try:
        #print(str(ii)+str((kline_data[f'{ii}']['open'].tolist()[1]-kline_data[f'{ii}']['open'].tolist()[0])/kline_data[f'{ii}']['open'].tolist()[0]*100))
        #这个是每个股票开盘一刻的涨幅
        zhangfu_dict[ii]=(kline_data[f'{ii}']['open'].tolist()[1]-kline_data[f'{ii}']['open'].tolist()[0])/kline_data[f'{ii}']['open'].tolist()[0]*100
        chengjiaoe_dict[ii] = kline_data[f'{ii}']['amount'].tolist()[0]
        time.sleep(0.1)
    except:
        pass
print(chengjiaoe_dict)
for i,ii in dict1.items():
    try:
        if chengjiaoe_dict[ii] < 700000:
            del zhangfu_dict[ii]
    except:
        pass

print(dict_rank(zhangfu_dict,'origin'))#这个是排序好的字典

