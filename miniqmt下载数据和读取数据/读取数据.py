from xtquant import xtdata
import pandas as pd
def market_data_into_format(code_list, data):
    """
    转换xtquant库返回的数据格式
    :return:dict
    """
    format_dict = {}
    for code in code_list:
        code_df = pd.DataFrame()
        for column_name in data.keys():
            column_df = data[column_name]
            code_df[column_name] = column_df.loc[code]
        format_dict[code] = code_df
    return format_dict
stock_list = ['123218.SZ','123106.SZ']
start_time = '20240411092500'
end_time = '20240411093100'
data = xtdata.get_market_data(field_list=[],
							  stock_list=stock_list,
							  period='1m',
							  start_time=start_time,
							  end_time= end_time,
							  count=1000,
							  dividend_type='none',
							  fill_data=True,)
data_dict = market_data_into_format(stock_list,data)
print(data_dict)