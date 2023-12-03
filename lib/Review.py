class Review:
    all = []
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        restaurant.reviews.append(self)
        Review.all.append(self)
    
    @property
    def rating(self):
        return self._rating
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        pass
    
    @property 
    def restaurant(self):
        return self._restaurant
    
    