import requests
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import sys

class VolData:
    def __init__(self, ticker, option_type='call', n=3):
        self.ticker = ticker
        self.option_type = option_type
        self.n = n

    def get_input_data(self):
        storage = []
        x = yf.Ticker(self.ticker)
        option_dates = x.options
        if len(option_dates) == 0:
            sys.exit("Ticker does not have any options. Please try another ticker")
        for date in tqdm(option_dates):
            try:
                call, put = x.option_chain(date)[0], x.option_chain(date)[1]
                call['option_type'], put['option_type'] = ('call', 'put')
                d = pd.concat([call, put])
                storage.append(d)
            except:
                pass
        df = pd.concat(storage)
        df = df.reset_index()
        df['maturity'] = pd.DataFrame([i[-15:-9] for i in df.contractSymbol])
        return df

    def plot_vol_smile(self):
        data = self.get_input_data()
        maturities = list(set(data.maturity))
        maturities.sort()
        for date in maturities:
            temp = data[(data.maturity == date) & (data.option_type == self.option_type)]
            title_date = datetime.date(2000 + int(date[:2]), int(date[2:4]), int(date[4:])).strftime("%B %d, %Y")
            plt.scatter(temp.strike, temp.impliedVolatility)
            plt.title(self.ticker.upper() + " " + self.option_type.upper() + ": " + title_date)
            plt.ylabel("Implied Volatility")
            plt.xlabel("Strike")
            plt.show()


    def plot_vol_term_structure(self):
        data = self.get_input_data()
        p = yf.Ticker(self.ticker).info
        mid_price = (p['ask'] + p['bid'])/2
        strikes = list(set(data.strike))
        maturities = list(set(data.maturity))

        get_closest_strike = min(range(len(strikes)), key=lambda i: abs(strikes[i]- mid_price))
        closest_ATM_indexes = list(range(get_closest_strike - self.n,
                                         get_closest_strike + self.n))
        closest_ATM_strikes = [strikes[i] for i in closest_ATM_indexes]
        storage = []
        for date in maturities:
            try: # NOTE - THE CALLS AND PUTS HERE ARE SEPERATED OUT - LOOK INTO HOW TO INCLUDE BOTH
                temp = data[(data.maturity == date) & (data.option_type== self.option_type)]
                storage.append(temp[temp['strike'].isin(closest_ATM_strikes)].mean()['impliedVolatility'])
            except:
                continue
        df = pd.DataFrame([maturities, storage]).T
        df = df.sort_values(0)
        df = df.dropna()
        plt.plot(df[0], df[1])
        plt.show()
