class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")


class Child(object):
    def __init__(self):
        # Initialises an instance of class Other and assign it to a variable.
        self.other=Other()
    def implicit(self):
        # implicit method calls the implicit method of 'other' instance.
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self): 
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
        
son=Child()
son.implicit()
son.override()
son.altered()