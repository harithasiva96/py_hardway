class Parent(object):
    # Parent class has a method called altered
    def altered(self):
        print("PARENT altered()")
class Child(Parent):
    # Child class ooverrides the altered function.
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # altered of parent class is called from within child class's  altered method
        super(Child,self).altered()
        print("CHILD, AFTER PARENT altered()")

dad=Parent()
son=Child()

dad.altered()
son.altered()