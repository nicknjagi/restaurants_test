from Review import Review
from Restaurant import *

class Customer:
    all = []
    
    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all.append(self)
    
    @property
    def given_name(self):
        return self._given_name
    
    @given_name.setter
    def given_name(self, value):
        self._given_name = value
    
    @property
    def family_name(self):
        return self._family_name
    
    @family_name.setter
    def family_name(self, value):
        self._family_name = value
    
    def full_name(self):
        return f"{self._given_name} {self._family_name}"
    
    @property
    def restaurants(self):
        return list(set([review.restaurant for review in Review.all if review.customer == self]))
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        return review
    
    def num_reviews(self):
        return len([review for review in Review.all if review.customer == self])
    
    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.all if customer.full_name() == name), None)
    
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all if customer._given_name == name or customer._family_name == name]
    
