"""
The Singleton pattern would indeed be useful for creating a single instance of the ParkingLot class, ensuring that there’s only one parking lot system in operation.
The Factory pattern could be used to create different types of parking spots based on vehicle type and floor level, providing flexibility in instantiation.
The Strategy pattern would be a good choice for handling payments, as it would allow for dynamic selection of payment methods and parking spot allocation strategies.
The Observer pattern would be useful for notifying the parking lot manager about the availability of parking spots, and the State pattern could be used to manage the states of the parking spots (free or occupied).
"""




# lets use composion over inheritance
class CarType:
    def description(self):
        pass

class Sedan(CarType):
    def description(self):
        return "Sedan: Comfortable and fuel-efficient."

class SUV(CarType):
    def description(self):
        return "SUV: Spacious and good for off-roading."

class SportsCar(CarType):
    def description(self):
        return "Sports Car: Fast and stylish."

class Car:
    def __init__(self, car_type):
        self.car_type = car_type

    def describe(self):
        return self.car_type.describe()