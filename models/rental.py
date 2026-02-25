# Handles rentals class
# Has number of days, total price, vehicle status (available or rented)
class Rental:
    rental_counter = 1

    # Initialise the above steps
    def __init__(self, user_id, vehicle_id, days):
        self.rental_id = Rental.rental_counter
        Rental.rental_counter += 1

        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.days = days
        self.status = "active"
        self.total_price = 0

    # Method for dict for the json
    def to_dict(self):
        return {
            "rental_id": self.rental_id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            "days": self.days,
            "status": self.status,
            "total_price": self.total_price
        }
    
rental_1 = Rental(1, 1, 5)
print(rental_1.to_dict())
print(rental_1.status)