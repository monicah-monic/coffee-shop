
class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            self._name = new_name
        else:
            return "Coffee name must be at least 3 characters."    

    
    def add_item(self, item):
        self.orders.append(item)
    
    def get_coffee_items(self):
        ordered = set()
        coffee_list = []
        for item in self.orders:
            if item not in ordered:
                coffee_list.append(item)
                ordered.add(item)
        return coffee_list
