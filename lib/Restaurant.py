class Restaurant:
    
    def __init__(self, name: str):
        self._name = name
        self._reviews = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        pass
    
    @property
    def reviews(self):
        return self._reviews
    
    @reviews.setter
    def reviews(self, value):
        self._reviews.append(value)
    
    @property
    def customers(self):
        return list(set([review.customer for review in self.reviews]))
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        
        total_rating = sum([review.rating for review in self.reviews])
        return total_rating / len(self.reviews)
    
