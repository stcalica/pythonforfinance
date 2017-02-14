import datetime as dt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

#properly import matplotlib and use proper backend graphics for mac 
import matplotlib as mil
mil.use('TkAgg')

import matplotlib.pyplot as plt

#Datetime will easily allow us to work with dates, matplotlib to graph things, pandas to manipulate data, and the pandas_datareader is the newest pandas io library at the time of my writing this.

#set up
style.use('ggplot')

#grab start and end times
start = dt.datetime(2000,1,1)
end =dt.datetime(2016, 12, 31)


#create a dataframe
df = web.DataReader('TSLA', "yahoo", start, end)

# uses the pandas_datareader package, looks for the stock ticker TSLA(Tesla), gets the information from yahoo, for the starting date of whatever start is and ends at the end variabl that we chose.
print(df.head())

#save to csv and read from csv
df.to_csv('TSLA.csv');
df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)

#plot and show data
df.plot()
plt.show()
