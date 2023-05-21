import yfinance as yf
import pandas as pd
import time
import datetime
import os

    ## Session information
current_directory = os.getcwd()
timestamp = time.strftime("%m-%d-%Y %H_%M")

    ## User Prompted for tickers
print("What Tickers would you like to download?")
print("Must be presented as a list that is NOT comma delimited (ie. SPY AAPL MSFT)")
print("Do not include any parenthesis or other characters")
user_requested_tickers = input("\n"+"Please input desired tickers:").capitalize()

    ## User prompted for period
print("\n"+"What period would you like data for?")
print("Possible values are 1D, 5D, 3M, 6M, YTD, 1Y, 5Y, Max")
user_requested_period = input("\n"+"Please input desired period:").capitalize()

    ## User prompted for interval
print("\n"+"What interval (frequency) would you like for your data?")
print("Possible values are 1d, 5d, 1wk, 1mo, 3mo")
user_requested_interval = input("\n"+"Please input desired interval:").lower()

    ## Download operation
yfdata = yf.download(
    f'{user_requested_tickers}', 
    repair = True, 
    show_errors = True, 
    period = f'{user_requested_period}', 
    interval = f'{user_requested_interval}'
    )

    ## Truncating and Removing unwanted data
yfdata_adjonly = yfdata.drop(['Close', 'High','Low', 'Open', 'Volume'], axis=1)
yfdata_returnsdata = yfdata_adjonly['Adj Close'].pct_change()
yfdata_returnsdata_trunc = yfdata_returnsdata.iloc[1:]

    ## Saving data to CSV files
yfdata.to_csv(f'{current_directory}/YFinance_alldata_{timestamp}.csv')
yfdata_returnsdata_trunc.to_csv(f'{current_directory}/YFinance_returnsonly_{timestamp}.csv')

    ## Final Message and user exit
print("\n"+f"Data has been saved to {current_directory} with names YFinance_alldata_{timestamp}.csv and YFinance_returnsonly_{timestamp}.csv")
exit_prg = input("\n"+"Press any key to exit:")
if exit_prg:
    exit()
