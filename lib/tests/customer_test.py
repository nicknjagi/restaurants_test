from Customer import Customer
from Review import Review
from Restaurant import Restaurant

class TestCustomer:
    
    def test_has_given_name_and_family_name(self):
        '''Customer is initialized with a given name and family name'''
        customer = Customer('Mike','Scott') # first Customer instance
        assert(customer.given_name == 'Mike')
        assert(customer.family_name == 'Scott')
        
    def test_names_can_change(self):
        '''Names are able to change after a customer is created'''
        customer = Customer('Mike','Scott') # second Customer instance
        customer.given_name = 'Jim'
        customer.family_name = 'Halpert'
        assert(customer.given_name == 'Jim')
        assert(customer.family_name == 'Halpert')
        
    def test_get_full_name(self):
        '''returns the full name of the customer, with the given name and the family name concatenated, Western style'''
        customer = Customer('Mike','Scott') # third Customer instance
        assert(customer.full_name() == 'Mike Scott')
        
    def test_get_all_customer_instances(self):
        '''returns all customer instances'''
        assert(len(Customer.all) == 3)
        
    def test_returns_unique_list_of_reviewed_restaurants(self):
        '''Returns a **unique** list of all restaurants a customer has reviewed'''
        cust1 = Customer('Pam','Beesly')
        rest1 =Restaurant('bobs burgers')
        rev1 = Review(cust1, rest1, 8)
        assert(cust1.restaurants == [rest1])
        
    def test_adds_review(self):
        '''given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant'''
        cust1 = Customer('Pam','Beesly')
        rest1 =Restaurant('bobs burgers')
        rev1 = Review(cust1, rest1, 8)
        assert(rev1.customer == cust1)
        
    def test_get_all_reviews(self):
        '''Returns the total number of reviews that a customer has authored'''
        cust1 = Customer('Pam','Beesly')
        rest1 =Restaurant('bobs burgers')
        rev1 = Review(cust1, rest1, 5)
        assert(cust1.num_reviews() == 1)

    def test_find_by_name(self):
        '''given a string of a **full name**, returns the **first customer** whose full name matches'''
        cust1 = Customer('Pam','Beesly')
        cust2 = Customer('Pam','Beesly')
        assert(Customer.find_by_name('Pam Beesly').__dict__ == cust1.__dict__)
        
    def test_find_by_all(self):
        '''given a string of a given name, returns an **list** containing all customers with that given name'''
        cust1 = Customer('Nick','Bee')
        cust2 = Customer('ger','Nick')
        assert(Customer.find_all_by_given_name('Nick') == [cust1,cust2])