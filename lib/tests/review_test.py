from Review import Review
from Customer import Customer
from Restaurant import Restaurant

class TestReview:
    
    def test_has_restaurant_rating(self):
        '''Reviews should be initialized with a customer, restaurant, and a rating (a number)'''
        customer1 = Customer('Mike', 'Scott')
        restaurant = Restaurant('kfc')
        review = Review(customer1,restaurant,4)
        assert(isinstance(review.customer, Customer) == True)
        assert(review.restaurant == restaurant)
        assert(review.rating == 4)
        
    def test_returns_rating(self):
        '''returns the rating for a restaurant.'''
        customer1 = Customer('Mike', 'Scott')
        restaurant = Restaurant('kfc')
        review = Review(customer1,restaurant,6)
        assert(review.rating == 6)
        
    def test_returns_all_reviews(Self):
        '''returns all of the reviews'''
        assert(len(Review.all) == 10)
        
    def test_returns_the_customer_object(self):
        '''returns the customer object for that review'''
        customer1 = Customer('Jim', 'Harper')
        restaurant = Restaurant('burger king')
        review = Review(customer1,restaurant,7)
        assert(review.customer == customer1)
        
    def test_returns_restaurant_obj(Self):
        '''returns the restaurant object for that given review'''
        customer1 = Customer('Mike', 'Scott')
        restaurant = Restaurant('kfc')
        review = Review(customer1,restaurant,6)
        assert(review.restaurant == restaurant)