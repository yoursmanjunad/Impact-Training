from abc import ABC, abstractmethod
class Television(ABC):
    def __init__(self, brand):
        self.brand = brand
        self.powerd_on= False

    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    @abstractmethod
    def chande_channel(self,channel):
        pass
class SmartTv(Television):
    def turn_on(self):
        self.powerd_on = True
        print(f"{self.brand} SmartTv is On.")
    def turn_off(self):
        self.powerd_on =False
        print(f"{self.brand} Smart Tv is OFF")
    def chande_channel(self,channel):
        if self.powerd_on:
            print(f"{self.brand} Smart Tv is now channel on {channel}")
        else:
            print("Cannot change channel. Tv is Off")
SmartTv = SmartTv(brand="LGBTQ")
SmartTv.turn_on()
SmartTv.chande_channel(5)
SmartTv.turn_off()