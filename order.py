from customer import Customer;
from coffee import Coffee;

class Order:
    def __init__(self, customer, coffee, price):
        self.customer =customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_name):
        if  isinstance(new_name, Customer):
            self._customer = new_name

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_name):
        if isinstance(new_name, Coffee):
            self._coffee = new_name

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price,(int, float)) and (1 <= price <= 10):
            self._price = price
        else:
            return "price must be between 1.0 and 10.0."    
        

if __name__ == "__main__":
    customer = Customer("Jane")
    coffee = Coffee("Cappuccino")
 
    order = customer.create_order(coffee, 3.00)

    print(f"Order created by: {order.customer.name}")
    print(f"Coffee: {order.coffee.name}, Price: ${order.price}")
    
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    customer1 = Customer("June")
    customer2 = Customer("Eunice")

    customer1.create_order(coffee1, 3.00)
    customer1.create_order(coffee1, 4.00)
    customer2.create_order(coffee1, 6.00)
    customer2.create_order(coffee2, 5.00)

    aficionado = Customer.most_aficionado(coffee1)
    if aficionado:
        print(f"The most aficionado for {coffee1.name} is: {aficionado.name}")
    else:
        print(None)





