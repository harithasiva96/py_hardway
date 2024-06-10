class Parent(object):
    def override(self):
        print("PARENT override()")
# A base class inherited from Parent class
class Child(Parent):
    def override(self):
        print("CHILD override()")
# Created instances dad and son      
dad=Parent()
son=Child()
# dad is an instance of parent and it is calls the override method of parent class.
dad.override()
son.override()