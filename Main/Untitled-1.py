import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

companay_list = r'D:\OneDrive\Documents\Test Reepository\Company_list.xlsx'
tsla = r'D:\OneDrive\Documents\Test Reepository\TSLA.csv'
nasdaq = r'D:\OneDrive\Documents\Test Reepository\nasdaq.csv'
f = r'D:\OneDrive\Documents\Test Reepository\F.csv'


dfCompany = pd.read_excel(companay_list)
dfTSLA = pd.read_csv(tsla)
dfNASDAQ = pd.read_csv(nasdaq)
dfF = pd.read_csv(f)

dfTSLA['Date'] = pd.to_datetime(dfTSLA['Date'])
dfTSLA.set_index('Date', inplace=True)

dfNASDAQ['Date'] = pd.to_datetime(dfNASDAQ['Date'])
dfNASDAQ.set_index('Date', inplace=True)

dfF['Date'] = pd.to_datetime(dfF['Date'])
dfF.set_index('Date', inplace=True)

dfTSLA['Close'] = pd.to_numeric(dfTSLA['Close'], errors='coerce')
dfNASDAQ['Close'] = pd.to_numeric(dfNASDAQ['Close'], errors='coerce')
dfF['Close'] = pd.to_numeric(dfF['Close'], errors='coerce')


'''dfTSLA['Open'].plot(x='Date', y='Open', kind='line')
plt.title('Bar Graph of Tsla Open Price')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()'''

dfTSLA['Close'].plot(x='Date', y='Close', kind='line')
plt.title('Bar Graph of Tsla Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()


dfNASDAQ['Close'].plot(x='Date', y='Close', kind='line')
plt.title('Bar Graph of NASDAQ Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()


dfF['Close'].plot(x='Date', y='Close', kind='line')
plt.title('Bar Graph of Ford Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()




plt.figure(figsize=(10, 6))
plt.plot(dfTSLA.index, dfTSLA['Close'], label='TSLA Close Price')
plt.plot(dfF.index, dfF['Close'], label='Ford Close Price')
plt.title('TSLA and Ford Close Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()