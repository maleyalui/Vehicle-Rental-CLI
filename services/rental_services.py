# Should handle Log in and Registration
# Import necessary dependencies
import json
import os
from models.rental import Rental
from services.vehicle_services import load_vehicles, save_vehicles

RENTAL_FILE = "data/rentals.json"

# Load rentals
def load_rentals():
    if not os.path.exists(RENTAL_FILE):
        return []

    with open(RENTAL_FILE, "r") as f:
        return json.load(f)

# Save rentals
def save_rentals(rentals):
    with open(RENTAL_FILE, "w") as f:
        json.dump(rentals, f, indent=4)

# Func to rent vehicle maximum of 2weeks(14days)
def rent_vehicle(user, vehicle_id, days):
    if days > 14:
        print("Maximum days for rental is 14.")
        return

    vehicles = load_vehicles()
    rentals = load_rentals()

    # update rental counter based on existing rentals
    if len(rentals) > 0:
        last_id = rentals[-1]["rental_id"]
        Rental.rental_counter = last_id + 1

    for v in vehicles:
        if v["id"] == vehicle_id and v["available"]:

            rental = Rental(user["id"], vehicle_id, days)
            rental.total_price = days * v["price_per_day"]

            rentals.append(rental.to_dict())
            v["available"] = False

            save_rentals(rentals)
            save_vehicles(vehicles)

            print(v["brand"], v["model"], "is rented for", days, "days.")
            print("Total price:", rental.total_price)
            return

    print("Not available")

# func to return vehicle i.e change status to returned
def return_vehicle(user, vehicle_id):
    vehicles = load_vehicles()
    rentals = load_rentals()

    for r in rentals:
        if r["vehicle_id"] == vehicle_id and r["user_id"] == user["id"] and r["status"] == "active":

            r["status"] = "returned"

            for v in vehicles:
                if v["id"] == vehicle_id:
                    v["available"] = True

            save_rentals(rentals)
            save_vehicles(vehicles)

            print("Vehicle returned")
            return

    print("Rental not found")