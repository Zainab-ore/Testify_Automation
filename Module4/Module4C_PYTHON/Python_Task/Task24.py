"""""
Create an abstract class called Vehicle
Create an abstract method called drive_direction()
Create another class Car that inherits from Vehicle
Create another class Plane that inherits from Vehicle
Try running the program and fix the abstract method issues

Optionally instantiate the Car and Plane method, then invoke the drive_direction() in each of the object instances.

Hint: the drive_direction() method in your Car should print "Drive forward", while drive_direction() in your Plane class should print "Drive Upward"""
import abc

# Abstract class Vehicle
class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod

    def drive_direction(self):
        pass

# Concrete class Car inheriting from Vehicle
class Car(Vehicle):
    def drive_direction(self):
        return "Drive forward"

# Concrete class Plane inheriting from Vehicle
class Plane(Vehicle):
    def drive_direction(self):
        return "Drive Upward"


# instantiate
vehicle_car = Car()
vehicle_plane = Plane()

# print
print(vehicle_car.drive_direction()) # Output: Drive forward
print(vehicle_plane.drive_direction()) # Output: Drive upward