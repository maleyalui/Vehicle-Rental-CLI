##Handles Vehicle classes 
# i.e Brand, model, price per day,availability
#vehicle id counter

class Vehicle:
    id_counter = 1

    #Initialise the steps above
    def __init__(self, brand, model, price_per_day):
        self.id = Vehicle.id_counter
        Vehicle.id_counter += 1

        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.available = True



    #A method to create a dict fo Json Storage
    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "price_per_day": self.price_per_day,
            "available": self.available
        }
#car1_=Vehicle("Toyota","Camry", 50.00)
#car2_=Vehicle("Honda", "Civic", 40.00)
#print(car1_.to_dict())
#print(car2_.to_dict())

   
    