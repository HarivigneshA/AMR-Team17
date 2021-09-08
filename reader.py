import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import mplfinance as mpf
import requests

class Reader():
    def __init__(self):
        self.df = pd.read_json('NT_OHLC/Stock List.json')

    def showChartByDates(self,kk,dt,de):
        df_google = self.df[self.df['symbol'] == kk].copy()
        df_google['date'] = pd.to_datetime(df_google['date'])
        df_google = df_google[df_google['date'] > pd.to_datetime(dt) ]
        df_google = df_google[df_google['date'] < pd.to_datetime(de) ]
        df_google = df_google.set_index('date')
        mpf.plot(df_google, savefig='chart.png')
        
    
    def showChartsBySymbol(self,kk):
        df_google = self.df[self.df['key'] == kk].copy()
        df_google['date'] = pd.to_datetime(df_google['date'])
        df_google = df_google.set_index('date')
        mpf.plot(df_google,savefig='chart.png')
        # fig = mpf.get_figure()
        # return fig

    def getCompanyInfo(self,symbol):

        url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token=pk_493f8953ec20439c95330df75f6eea49'
        r = requests.get(url = url)
        print(r)
        CompanyInfoJson = r.json()

