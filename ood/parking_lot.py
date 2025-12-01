"""
The Singleton pattern would indeed be useful for creating a single instance of the ParkingLot class, ensuring that there’s only one parking lot system in operation.
The Factory pattern could be used to create different types of parking spots based on vehicle type and floor level, providing flexibility in instantiation.
The Strategy pattern would be a good choice for handling payments, as it would allow for dynamic selection of payment methods and parking spot allocation strategies.
The Observer pattern would be useful for notifying the parking lot manager about the availability of parking spots, and the State pattern could be used to manage the states of the parking spots (free or occupied).
"""

from abc import ABC, abstractmethod
from enum import Enum


# start with constants and enums
class PaymentStatus(Enum):
    COMPLETED = 1
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5


# Custom Person data type class
class Person:
    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email


# Custom Address data type class
class Address:
    def __init__(self, zip_code, address, city, state, country):
        self.__zip_code = zip_code
        self.__address = address
        self.__city = city
        self.__state = state
        self.__country = country


# define parking spots
class ParkingSpot(ABC):
    def __init__(self, id, isFree, vehicle):
        self.__id = id
        self.__isFree = isFree
        self.__vehicle = vehicle  # Refers to an instance of the Vehicle class

    def get_is_free(self):
        pass

    @abstractmethod
    def assign_vehicle(self, vehicle):
        pass

    def remove_vehicle(self):
        pass


class Handicapped(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)

    def assign_vehicle(self, vehicle):
        pass


class Compact(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)

    def assign_vehicle(self, vehicle):
        pass


class Large(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)

    def assign_vehicle(self, vehicle):
        pass


class Motorcycle(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)

    def assign_vehicle(self, vehicle):
        pass


# define the vehicle classes
class Vehicle(ABC):
    def __init__(self, license_no):
        self.__license_no = license_no

    # ticket here refers to an instance of the ParkingTicket class
    @abstractmethod
    def assign_ticket(self, ticket):
        pass


class Car(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no)

    def assign_ticket(self, ticket):
        pass


class Van(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no)

    def assign_ticket(self, ticket):
        pass


class Truck(Vehicle):
    def __init__(self, license_no, ticket):
        super().__init__(license_no, ticket)

    def assign_ticket(self, ticket):
        pass


class MotorCycle(Vehicle):
    def __init__(self, license_no, ticket):
        super().__init__(license_no, ticket)

    def assign_ticket(self, ticket):
        pass


# define the account logic
class Account(ABC):
    # Data members
    def __init__(self, user_name, password, person, status):
        self.__user_name = user_name
        self.__password = password
        self.__person = person  # Refers to an instance of the Person class
        self.__status = status  # Refers to the AccountStatus enum

    @abstractmethod
    def reset_password(self):
        pass


class Admin(Account):
    def __init__(self, user_name, password, person, status):
        super().__init__(user_name, password, person, status)

    def add_parking_spot(self, spot):
        pass

    def add_display_board(self, display_board):
        pass

    def add_entrance(self, entrance):
        pass

    def add_exit(self, exit):
        pass

    def reset_password(self):
        pass


class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status):
        super().__init__(user_name, password, person, status)

    def process_ticket(self, ticket_number):
        pass

    def reset_password(self):
        pass


# define the display board and hour rate logic
class DisplayBoard:
    def __init__(self, id):
        self.__id = id
        self.__parking_spots = {}

    # Member functions
    def add_parking_spot(self, spot_type, spots):
        pass

    def show_free_slot(self):
        pass


class ParkinRate:
    def __init__(self, hours, rate):
        self.__hours = hours
        self.__rate = rate

    # Member function
    def calculate(self):
        pass


# entrance and exit logic
class Entrance:
    def __init__(self, id, ticket):
        self.__id = id

    def get_ticket(self):
        pass


class Exit:
    def __init__(self, id, ticket):
        self.__id = id

    def validate_ticket(self, ticket):
        # Perform validation logic for the parking ticket
        # Calculate parking charges, if necessary
        # Handle the exit process
        pass


# define the parking ticket logic
class ParkingTicket:
    def __init__(
        self,
        ticket_no,
        timestamp,
        exit,
        amount,
        status,
        vehicle,
        payment,
        entrance,
        exit_ins,
    ):
        self.__ticket_no = ticket_no
        self.__timestamp = timestamp
        self.__exit = exit
        self.__amount = amount
        self.__status = status

        # Following are the instances of their respective classes
        self.__vehicle = vehicle
        self.__payment = payment
        self.__entrance = entrance
        self.__exit_ins = exit_ins


# The __ParkingLot is a singleton class that ensures it will have only one active instance at a time
# Both the Entrance and Exit classes use this class to create and close parking tickets
class __ParkingLot(object):
    __instances = None

    def __new__(cls):
        # singleton logic
        if cls.__instances is None:
            cls.__instances = super(__ParkingLot, cls).__new__(cls)
        return cls.__instances


class ParkingLot(metaclass=__ParkingLot):
    def __init__(self, id, name, address, parking_rate):
        # Call the name, address and parking_rate
        self.__id = id
        self.__name = name
        self.__address = address
        self.__parking_rate = parking_rate

        # Create initial entrance and exit hashmaps respectively
        self.__entrance = {}
        self.__exit = {}

        # Create a hashmap that identifies all currently generated tickets using their ticket number
        self.__tickets = {}

    # entrance here refers to an instance of the Entrance class
    def add_entrance(self, entrance):
        pass

    # exit here refers to an instance of the Exit class
    def add_exit(self, exit):
        pass

    # This function allows parking tickets to be available at multiple entrances
    # vehicle here refers to an instance of the Vehicle class
    # Returns a ParkingTicket instance
    def get_parking_ticket(self, vehicle):
        pass

    # type here refers to an instance of the ParkingSpot class
    def is_full(self, type):
        pass
