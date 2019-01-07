# EZoptions
Python Library for Options Analysis


Author: Matija Krolo



## Current Features:
1.) Black-Scholes Model on Equities Trading on Robinhood (For Call Options) (<a>https://robinhood.com/</a>)
```python
bsm_robinhood_equties( ticker, strike price, days to maturity, diagnostics (optional: True/False) )
bsm_robinhood_equtities('NFLX', 250, 60, False)
```

For feature requests, please email krolo@wisc.edu

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
