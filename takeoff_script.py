from dronekit import connect, VehicleMode

# Connect to the vehicle
vehicle = connect('udpin:0.0.0.0:14550',wait_ready=True)

# Arm the vehicle and take off to a target altitude of 10 meters
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.simple_takeoff(5)

# Wait for the vehicle to reach the target altitude
while True:
    altitude = vehicle.location.global_relative_frame.alt
    if altitude >= 5 * 0.95:
        break

# Print a message to indicate that the vehicle has reached the target altitude
print("Vehicle has reached target altitude")

# Close the connection
vehicle.close()

