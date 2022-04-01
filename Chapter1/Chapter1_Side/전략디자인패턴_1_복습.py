import abc


class Duck:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.fly_behavior.fly()

    def performQuack(self):
        self.quack_behavior.quack()


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoway()
        self.quack_behavior = Quack()

    def display(self):
        print("Mallard duck")


class FlyBehavior:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fly(self):
        pass


class FlyNoway(FlyBehavior):
    def fly(self):
        print("Fly no way")


class QuackBehavior:
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack Quack")


mallad_duck = MallardDuck()

print("#MALLAD DUCK#")
mallad_duck.display()
mallad_duck.performFly()
mallad_duck.performQuack()
