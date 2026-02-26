#Handle Vehicle operations

## IMPORT REQUIRED DEPENDANCIES
import json
import os
from models.vehicle import Vehicle

VEHICLE_FILE = "data/vehicles.json"

#Load vehicles
def load_vehicles():
    if not os.path.exists(VEHICLE_FILE):
        return []
    with open(VEHICLE_FILE, "r") as f:
        return json.load(f)

#save vehilces
def save_vehicles(vehicles):
    os.makedirs(os.path.dirname(VEHICLE_FILE), exist_ok=True)
    with open(VEHICLE_FILE, "w") as f:
        json.dump(vehicles, f, indent=4)

# (FOR ADMIN ) add new vehicle
def add_vehicle(brand, model, price):
    vehicles = load_vehicles()

    new_vehicle = Vehicle(brand, model, price)
    vehicles.append(new_vehicle.to_dict())
    save_vehicles(vehicles)

    print("Vehicle added successfully!")
# func List all vehicles i.e status brand model price availability
def list_vehicles():
    vehicles = load_vehicles()

    if not vehicles:
        print("No vehicles found.")
        return

    for v in vehicles:
        status = "Available" if v["available"] else "Rented"
        print(f"{v['id']} - {v['brand']} {v['model']} - {status} - {v['price_per_day']} per day")


# Test 1: Add a new vehicle
# print("--- Adding Vehicles ---")
# add_vehicle("Toyota", "Camry", 50)
# add_vehicle("Tesla", "Model 3", 100)

# # Test 2: List the vehicles to verify they were saved and loaded
# print("\n--- Listing Vehicles ---")
# list_vehicles()








