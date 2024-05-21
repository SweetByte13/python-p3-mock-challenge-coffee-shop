class Coffee:
    all=[]
    
    def __init__(self, name):
        self.name = name
        Coffee.add_new_coffee(self)
        
    @classmethod
    def add_new_coffee(cls, new_coffee):
        cls.all.append(new_coffee)  
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self,'_name') and isinstance(new_name, str) and 3 <= len(new_name):
            self._name = new_name
            
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        unique_list = set([order.customer for order in Order.all if order.coffee == self])
        return list(unique_list)
    
    def num_orders(self):
         count_of_orders=[order.coffee for order in Order.all if order.coffee == self]
         return len(count_of_orders)
    
    def average_price(self):
        price_total = [order.price for order in Order.all if order.coffee == self]
        return(sum(price_total)/len(price_total))
         


class Customer:
    all=[]
    
    def __init__(self, name):
        self._name = name
        Customer.add_new_customer(self)
        
    @classmethod
    def add_new_customer(cls, new_customer):
        cls.all.append(new_customer)   
         
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_list = set([order.coffee for order in Order.all if order.customer == self])
        return list(unique_list)
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
    
    
class Order:
    all=[]
    
    def __init__(self, customer, coffee, price):
            self._price = price
            self._customer = customer
            self._coffee = coffee
            Order.add_new_order(self)
            
    @classmethod
    def add_new_order(cls, new_order):
        cls.all.append(new_order)
            
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and 1.0 <= (new_price) <= 10.0 and not hasattr(self,'_price'):
            self._price = new_price
            
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,customer):
        if isinstance(self, Customer):
            self._customer = customer
            
    @property
    def coffee(self):
        return self._coffee
        
    @coffee.setter
    def coffee(self,coffee):
        if isinstance(self, Coffee):
            self._coffee = coffee
            
    