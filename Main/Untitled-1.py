import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

companay_list = r'D:\OneDrive\Documents\Test Reepository\Company_list.xlsx'
tsla = r'D:\OneDrive\Documents\Test Reepository\TSLA.csv'

dfCompany = pd.read_excel(companay_list)
dfTSLA = pd.read_csv(tsla)

dfTSLA['Date'] = pd.to_datetime(dfTSLA['Date'])
dfTSLA.set_index('Date', inplace=True)

dfTSLA['Open'].plot(x='Date', y='Open', kind='line')
plt.title('Bar Graph of Tsla Open Price')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

dfTSLA['Close'].plot(x='Date', y='Close', kind='line')
plt.title('Bar Graph of Tsla Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()