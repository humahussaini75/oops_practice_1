class Parent_Class( object ):
    def __init__(self):
        pass


class Child_Class( Parent_Class ):
    def __init__(self):
        super().__init__()


class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"  #it takes this first, since it goes step by step
        self.classvar1 = "Instance var in class B"  # then it takes this since this is second step
        super().__init__()  #now calling the super constructor
        print(super().classvar1)  #we are printing here, thats why it is giveing super class var. if no print statment then it will print var1 and classvar1of class b
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"

#a = A()
b = B()

print(b.special, b.var1, b.classvar1)
