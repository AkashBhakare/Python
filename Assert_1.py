# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:42:33 2021

@author: Akash
"""

# Basic Assertion

import sys

# Don’t Use Asserts for Data Validation
def ConvertKmToMtr(distKm:float)->float:
    from typing import Final
    KM_TO_MTR_FACTOR:Final[float] = 1000.0
    assert(distKm > 0),"Distance should be Positive Nonzero Value"
    distMtr = distKm * KM_TO_MTR_FACTOR
    return distMtr


def ConvertKmToMtr_improved(distKm):
    
    if (distKm < 0):
        raise ValueError("Distance should be Positive Nonzero Value")
        
    from typing import Final    
    KM_TO_MTR_FACTOR:Final[float] = 1000.0
    distMtr = distKm * KM_TO_MTR_FACTOR
    return round(distMtr,2)


if __name__=='__main__':
    try:
        distkm = float(input('Please enter the distance in Kilometers:'))
        distmtr = ConvertKmToMtr(distkm)
        print(f"{distkm} km = {distmtr} mtrs")
        
        distmtr = ConvertKmToMtr_improved(distkm)
        import math      
        assert(distmtr == math.fabs(distkm*1000)), "Big Mistake Shardul"
        if(distmtr != distkm*1000.00):
            print("Sharudl ! You have failed me!")
            
        print(f'Distance in Meters is {distmtr:.2f} mtrs')
    except AssertionError as error:
         print(error,file=sys.stderr)
    except ValueError as ve:
        print(ve,file=sys.stderr)
