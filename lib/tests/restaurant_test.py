from Restaurant import Restaurant
from Review import Review
from Customer import Customer

class TestRestaurant:
    
    def test_has_unchangeable_name_as_a_string(self):
        '''restaurant is initialized with a name'''
        restaurant = Restaurant('chipotle')
        restaurant.name = 'burger king'
        assert(restaurant.name == 'chipotle')
        
    def test_returns_all_reviews(self):
        '''returns a list of all reviews for that restaurant'''
        cust1 = Customer('Mike','Scott')
        restaurant = Restaurant('burger king')
        review1 = Review(cust1,restaurant,8) 
        assert(len(restaurant.reviews) == 1)

    def test_returns_unique_customers(self):
        '''Returns a **unique** list of all customers who have reviewed a particular restaurant.'''
        cust1 = Customer('Mike','Scott')
        cust2 = Customer('Jim','Halpert')
        restaurant = Restaurant('jimmýs')
        review1 = Review(cust1,restaurant,8) 
        review2 = Review(cust2,restaurant,7) 
        assert(len(restaurant.customers) == 2)
        
    def test_average_rating(self):
        '''returns the average star rating for a restaurant based on its reviews'''
        cust1 = Customer('Mike','Scott')
        cust2 = Customer('Jim','Halpert')
        restaurant = Restaurant('jimms')
        review1 = Review(cust1,restaurant,8) 
        review2 = Review(cust2,restaurant,4) 
        assert(restaurant.average_star_rating() == 6)