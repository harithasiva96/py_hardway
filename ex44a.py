# Parent is a base class with a function implicit
class Parent(object):
    def implicit(self):
        print("PARENT implicit()")
# Child is a subclass inherited from Parent.
class Child(Parent):
    pass
# Class Parent is assigned to a variable dad
dad=Parent()
# Class Child is  assigned to a variable son
son=Child()
# implicit function is called with each classes parent and child.
dad.implicit()
son.implicit()
