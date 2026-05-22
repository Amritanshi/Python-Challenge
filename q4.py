#  A traffic monitoring system needs to determine whether a vehicle exceeded the speed limit.
speed_limit = 60
vehicle_speed = float(input("Enter the vehicle's speed: "))

if vehicle_speed > speed_limit:
    print("Vehicle has exceeded the speed limit.")
else:
    print("Vehicle is within the speed limit.")