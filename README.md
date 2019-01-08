# EZoptions
Python Library for Options Analysis


Author: Matija Krolo



## Current Features:
1.) Black-Scholes Model on Equities Trading on Robinhood (For Call Options) (<a>https://robinhood.com/</a>)
```python
bsm_robinhood_equties( ticker, strike price, days to maturity, diagnostics (optional: True/False), custom volatility input (optional )

# To find the call value on Netflix with an excercise price of $250 and 60 days to maturity (using market volatility and risk-free rates)
bsm_robinhood_equtities('NFLX', 250, 60, False)

# To find the call value on Netflix and assigning it to the variable 'nflx_value' with an excercise price of $250 and 60 days to maturity (using a custom implied volatlity of 25%)
nflx_value = bsm_robinhood_equtities('NFLX', 250, 60, False, 25)
```


## To use:
1.) Clone the master file (EZoptions.py) to your project directory


2.) Import the library
```python
from EZoptions import *
```

3.) Call an available library function. This may be assigned to a variable for data manipulation or simply printed. 
```python
# This prints the option value on a call option for Netflix with a strike price of $250 with 60 days to maturity
bsm_robinhood_equtities('NFLX', 250, 60, False)
>> Black Scholes Model Call Valued on NFLX: 37.81

# This assigns the optional value on a call option for Netflix with a strike price of $250 with 60 days to maturity to the variable 'nflx_value'
nflx_value = bsm_robinhood_equtities('NFLX', 250, 60, False)
>> 37.81
```

## Planned Features
1.) Custom Volatility Inputs


2.) Models for put options


3.) Additional languages/markets


4.) GUI/Front-facing web-app



## For feature requests, please email krolo@wisc.edu
