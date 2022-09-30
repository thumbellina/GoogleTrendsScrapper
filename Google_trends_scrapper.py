import pandas as pd
import pytrends
from pytrends import dailydata
from pytrends.request import TrendReq
import time

keywords=["bitcoin"]
date_start='2015-01-01'

startTime = time.time()
pytrend = TrendReq()


def clean(data_frame):
	data_frame.drop(columns=['isPartial'],inplace=True)
	data_frame.reset_index(level=0,inplace=True)

	return data_frame



try:
	# weekly data
	# first 2 years
	pytrend.build_payload(kw_list=keywords,timeframe='2015-01-01 2017-10-01') # location/category specific data can be customized through options
	df_15_17=pytrend.interest_over_time()
	# last 5 years
	pytrend.build_payload(kw_list=keywords,timeframe='today 5-y')
	df_5year =pytrend.interest_over_time()
    
	merged_weekly=pd.concat([clean(df_15_17),clean(df_5year)],ignore_index=True)
	merged_weekly.to_csv('search_trends_weekly.csv',index=False) 


	# daily data
	df_daily= dailydata.get_daily_data(keywords[0], start_year=2015, start_mon=1, stop_year=2022, stop_mon=9)
	clean(df_daily).to_csv('search_trends_daily.csv',index=False)


	# hourly data 
	pytrend = TrendReq()
	hourly_df = pytrend.get_historical_interest(keywords, year_start=2015,
                                             month_start=1, day_start=1,
                                             hour_start=0, year_end=2022,
                                             month_end=9, day_end=30, hour_end=0,
                                             )
	clean(hourly_df).to_csv('search_trends_hourly.csv',index=False)
except Exception as e: 
	print(e)

