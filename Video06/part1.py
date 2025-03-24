from abc import ABC, abstractmethod
# This is OOP in Pyhton
"""
            Animal
            /    \
    Carnivore     Herbivore"
        /           \
    Lion            Cow
     /                 \
  OBJ                   OBJ
"""


class Animal(ABC):

    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eats(self):
        pass


class Carnivore(Animal):
    def sound(self):
        print("??????")

    def eats(self):
        print("Carnivores Eat Meat")


class Lion(Carnivore):
    def __init__(self, kidsPerDelivery=1):
        super().__init__()
        self.__kidsPerDelivery = kidsPerDelivery

    def eats(self):
        print("Lions Eat Meat")

    def avgKidsPerDelivery(self):
        print("Delivers at once: "+str(self.__kidsPerDelivery)+" kids")

    def sound(self):
        print("Lions sound like: RooR")


class Herbivore(Animal):

    def sound(self):
        print("??????")

    def eats(self):
        print("Herbivores Eat Plant")


class Cow(Herbivore):
    """
        Cow class is derived from Herbivore Class\n
        Takes one argument:\n
        @kidsPerDelivery: number of children per delivery
    """

    def __init__(self, kidsPerDelivery=1):
        super().__init__()
        self.kidsPerDelivery = kidsPerDelivery

    def avgKidsPerDelivery(self):
        print("Delivers at once: "+str(self.kidsPerDelivery)+" kids")

    def eats(self):
        print("Cows Eat Plant")

    def sound(self):
        print("Cows sound like: Mooo")


class WhiteLion(Lion):
    def doSomthing(self):
        print(self.__kidsPerDelivery)


obj = Cow(2)

print(isinstance(obj, Cow))
print(isinstance(obj, Herbivore))
print(isinstance(obj, Animal))
print(isinstance(obj, Carnivore))

# obj = WhiteLion()
# obj.doSomthing()
