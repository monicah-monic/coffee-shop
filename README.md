# coffee shop
A project that implements domain modelling of a coffee shop using OOP principles


# Overview
A customer place many coffee orders - one to many relationship
A coffee can have many orders- one to many relationship
Customer and coffee have many to many relationship via oreders.

# classes
Has three files containing  customer,coffee and orders.
Customer class has name attribute and a list of orders
It has methods in customer file  :create order- creates an order for customer,add-order:adds to an existing order to customer and get orders-returns a list of all customer orders
coffee class: adds item-adds order to associated with coffee and get coffee-returns a list of orders for the coffee
order file:imports from customer and coffee classes, has customer,coffee and price attributes It also  returns  the output of our project                                          