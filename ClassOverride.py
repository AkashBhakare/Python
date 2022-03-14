# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 09:54:25 2021

@author: Akash
"""

## Orerriding methods

class Car(object):
    
    def __init__(self,model,price):
        self.__model = model
        self.__price = price
        
    def getModel(self):
        return self.__model
    
    def getPrice(self):
        return self.__price
    
    # Overriding the __str__() inherited from object
    def __str__(self):
        return f"Model: {self.__model},  Price: {self.__price}"



class RacingCar(Car):
    def __init__(self,model,price,is_nitro_booster:bool):
        super().__init__(model,price)
        self.__has_introBooster = is_nitro_booster
        
    def boostSpeed(self):
        print("Boosting the speed")
     
    #Racing car is not forced to override the __str__()
               
class ElectricCar(Car):
    
    def __init__(self,model,price,battery_cap):
        super().__init__(model,price)
        self.__batteryCapacity = battery_cap
    
    def chargeCar(self):
        print("Charging the Car!")
    
    # Overriding the __str__() inherited from Car
    def __str__(self):
        info = super().__str__()
        return f"{info},  Battery Capacity: {self.__batteryCapacity}"
        
            
if __name__ == '__main__':
    aCar = Car("XYZ",1234567)
    print("Model : ",aCar.getModel())
    print("Price : ",aCar.getPrice())
    print(aCar)
    # print()
    print(aCar.__str__())
    ecar = ElectricCar("Tesla",12345678,500)
    ecar.chargeCar()
    ecar.boostSpeed()
    print(ecar.getModel())
    print(ecar)
    print(ecar.__class__)