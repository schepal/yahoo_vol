# Options Volatility Analysis
A tool using the Yahoo Finance API to help visualize the implied volatility of an options chain. 

## Disclaimer - Please Read This First
This project is only for educational purposes and should not be relied on for live trading. There are several bugs in the Yahoo Finance API itself which causes the implied volatilities to sometimes be incorrect. Notably, most of the errors produced by the API are found when calling the function during after-market hours. In the case a particular options chain cannot be downloaded, there will be a prompt indicating the specific maturity that is missing.

### Current Features
- **Volatility Smile Visualizer**: According to the Black-Scholes model, options of the same maturity should theoretically have constant volatility across all strikes. However, for a variety of reasons, there tends to be a "smile-like" phenomenon in the implied volatility curve. This plotting function can be used to visualize the implied volatility of both call and put options against their respective strike values.

- **Volatility Term Structure Visualizer**: The volatility term structure can be used to indicate where the market as a whole believes future volatility will be in the future. There is a parameter in this function called ![$n$](https://render.githubusercontent.com/render/math?math=%24n%24) which allows a user to select ![$\pm n$](https://render.githubusercontent.com/render/math?math=%24%5Cpm%20n%24) options nearest to the at-the-money (ATM) option. For example, assuming the strikes of an option are separated by $1, if ![$\n=3$](https://render.githubusercontent.com/render/math?math=%24%5Cn%3D3%24) Copy
 and the ATM Price=100, then the following six strikes will be used for calculating the implied volatility term structure: a) Lower ATM: 97, 98, 99 b) Upper ATM: 101, 102, 103. The average implied volatility of all six options will be taken for each point on the term structure. This process is repeated for each tenor on the term structure.

## Example
``` python
>>> import yahoo_vol as vol
>>> data = vol.VolData("AAPL", n=3)

# Retrieves all option data for AAPL stock (both calls and puts) 
>>> df = data.get_input_data(save_csv=False)

>>> df.columns()
    Index(['index', 'contractSymbol', 'lastTradeDate', 'strike', 'lastPrice',
           'bid', 'ask', 'change', 'percentChange', 'volume', 'openInterest',
           'impliedVolatility', 'inTheMoney', 'contractSize', 'currency',
           'option_type', 'maturity'],
          dtype='object')
          
>>> df[['contractSymbol', 'option_type', 'strike']].head()
    contractSymbol	option_type	strike
    0	SPY200529C00150000	call	150.0
    1	SPY200529C00155000	call	155.0
    2	SPY200529C00190000	call	190.0
    3	SPY200529C00195000	call	195.0
    4	SPY200529C00200000	call	200.0

# Plot Volatility Smile
>>> data.plot_vol_smile()

# Plot Volatility Term Structure
>>> data.plot_vol_term_structure()
```

### Dependencies
- pandas==1.0.3
- matplotlib==3.2.1
- yfinance==0.1.54
- requests==2.21.0
- numpy==1.17.3
- tqdm==4.38.0

