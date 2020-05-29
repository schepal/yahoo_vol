# Options Volatility Analysis
A tool using the Yahoo Finance API to help visualize the implied volatility of an options chain. 

# Disclaimer - Please Read This First
This project is only for educational purposes and should not be relied on for live trading. There are several bugs in the Yahoo Finance API itself which causes the implied volatilities to sometimes be incorrect. Notably, most of the errors produced by the API are found when calling the function during after-market hours. In the case a particular options chain cannot be downloaded, there will be a prompt indicating the specific maturity that is missing.

### Current Features
- **Volatility Smile Visualizer**: According to the Black-Scholes model, options of the same maturity should theoretically have constant volatility across all strikes. However, for a variety of reasons, there tends to be a "smile-like" phenomenon in the implied volatility curve. This plotting function can be used to visualize the implied volatility of both call and put options against their respective strike values.

- **Volatility Term Structure Visualizer**: The volatility term structure can be used to indicate where the market as a whole believes future volatility will be in the future. There is a parameter in this function called $n$ which allows a user to select $+/-n$ options nearest to the at-the-money (ATM) option. For example, assuming the strikes of an option are available at 1 strike differences, if n=3 and the ATM Price=100, then the following 6 strikes will be used for calculating the implied volatility term structure: a) Lower ATM: 97, 98, 99 b) Upper ATM: 101, 102, 103. The average implied volatility of all six options will be taken for each maturity. This process is repeated for each other date on the term structure plot. 


