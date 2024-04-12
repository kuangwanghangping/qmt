from xtquant import xtdata
import pandas as pd
def on_progress(data):
	print(data)
stock_list = ['123218.SZ','123106.SZ']
start_time = '20240411092500'
end_time = '20240411093100'
xtdata.download_history_data2(stock_list=stock_list, period='1m', start_time=start_time, end_time=end_time, callback=on_progress)