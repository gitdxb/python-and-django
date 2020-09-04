class Animal():

    def __init__(self):
        print('Parent class started:')
        print('Animal created')

    def whoami(self):
        print('Animal')

    def eat(self):
        print('Eating')

doga = Animal()
doga.whoami()

# Inheritance

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)  => Output: Animal created
        print('\nChild class created:')
        print('Dog created')

    def bark(self):
        print('Woof')

    def eat(self):
        print('Dog eating')
        # This will overwrite parent class method

dogb = Dog()
dogb.bark()
dogb.eat()
