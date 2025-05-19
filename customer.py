class Customer:
    all_customers= []

    def __init__(self, name):
        self.name = name
        self.orders = []
        Customer.all_customers.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1<= len(new_name) <= 15:
            self._name = new_name
        else:
            return "Name must be a string between 1 and 15 characters"    

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)  # Create a new Order instance
        self.orders.append(order)  # Associate the order with the customer
        return order

    def add_order(self, order):
        return self.orders.append(order)
    
    
    def get_orders(self):
        return self.orders
    
    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        max_spend = 0

        for customer in cls.all_customers:
            total = sum(order.price for order in customer.orders if order.coffee == coffee)

            if total > max_spend:
                max_spent = total
                top_customer = customer

        return top_customer if max_spent > 0 else None
    


        
