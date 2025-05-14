from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

# Create a new instance of Vehicle
my_vehicle = Car("medium", 4)

# Test the attributes
print(f"Wheel size: {my_vehicle.wheel_size}")
print(f"Wheel number: {my_vehicle.wheel_number}")

# Test the methods
print(my_vehicle.go())
print(my_vehicle.fill_up_tank())
