# Easy Option Pricing Modules Library
# Currenly Supports The Black Scholes Model (European Calls) on Equities Through Robinhood's API
# By Matija Krolo
#
# To use:
# 1.) Import the library 
#		from ezoptions.py import *
# 2.) Call Any Available Library Functions:
#   	bsm_robinhood_equtities(Ticker, Strike Price, Days Until Maturity, Optional: Function Diagnostics, Optional: Custom Volatility Inputs)
#		ex:  bsm_robinhood_equtities('NFLX', 250, 60, False)
#
# Model Price Can Also Be Assigned To Any Variable For Manipulation
# 
# PFE_Fair_Value = bsm_robinhood_equities('PFE', 39, 60, False, 20)
#  
# Ezoptions requires the Pandas and Scipy libraries
#

# Import Libraries 
import pandas_datareader.data as web
from scipy import stats
import datetime as dt
from math import *

# Black Scholes Model for Robinhood's Equity Optinos
def bsm_robinhood_equtities(
    ticker, # Equity Ticker (ex. PFE, BRK.A)
    strike_price, # Excerciseable Price on Option
    days_to_maturity, # Time to Option Maturity (in days)
    diagnostics = False, # Optional Data on what the function uses
    optional_volatility = -1	#Custom Volatility Input
    ):
    try:
    	# Gather Model Data
    	custom_volatility_input = False
        time_to_maturity = round(days_to_maturity / 365.0, 10) # Annualize Time to Maturity 
        risk_free_rate = web.DataReader('DGS10', data_source="fred").tail(1) / 100 # Fetch Current Risk-Free Rate from https://fred.stlouisfed.org
        price_level = web.DataReader(ticker, 'robinhood').tail(1) # Fetch Latest Trading Data on Desired Equity
        load_diagnostics = price_level # Store Raw Data for Diagnostics Purposes
        price_level = price_level['close_price'].tolist()[0] 
        # Fetch Data on Implied Volatility Through the $VIX Index (plan on adding custom volatility inputs down the road)
        total_mkt_implied_volatility = web.DataReader('VIXCLS', data_source="fred"
                ).tail(1)
        price_level = float(price_level)
        if(optional_volatility != -1):
        	total_mkt_implied_volatility = (optional_volatility / 100.0)
        	custom_volatility_input = True
        else:
	        total_mkt_implied_volatility = \
	            float(total_mkt_implied_volatility['VIXCLS'] / 100)
        # Calculate Option Value based on the BSM (first d1, then d2) and manipulate data for output
        d1 = log(price_level / strike_price) + (risk_free_rate + .5
                * total_mkt_implied_volatility ** 2) * time_to_maturity \
            / (total_mkt_implied_volatility * sqrt(time_to_maturity))
        d1 = float(d1['DGS10'])
        d2 = log(price_level / strike_price) + (risk_free_rate - .5
                * total_mkt_implied_volatility ** 2) * time_to_maturity \
            / (total_mkt_implied_volatility * sqrt(time_to_maturity))
        d2 = float(d2['DGS10'])
        risk_free_rate = float(risk_free_rate['DGS10'])
        option_quote = round(price_level * stats.norm.cdf(d1, 0.0, 1.0)
                             - strike_price * exp(-risk_free_rate
                             * time_to_maturity) * stats.norm.cdf(d2,
                             0.0, 1.0), 2)
        # Optional Diagnostics Output
        if diagnostics:
            print 'Data from Robinhood API: '
            print load_diagnostics
            print '--------------\n\n'
            print 'Approx Spot Price (close): $' + str(price_level)
            print 'Strike Price: $' + str(strike_price) 
            print 'Risk free rate (FRED API): ' + str(risk_free_rate
                    * 100) + '%'
            if custom_volatility_input:
            	print '** Note: Implied Volatility was Input **'
            print 'Volatility: ' \
                + str(total_mkt_implied_volatility * 100) + '%'
        print 'Black Scholes Model Call Value on ' + ticker + ': $' + str(option_quote) + '\n\n'
        return option_quote
    # Catch Any Exceptions (Common error: Unavailable Equity)
    except:
        print 'Sorry, there was an error'
        return 0
