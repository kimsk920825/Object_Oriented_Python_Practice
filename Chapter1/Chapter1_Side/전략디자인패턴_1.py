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


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Fly with wings")


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


class MuteQuack(QuackBehavior):
    def quack(self):
        print("Mute...")


mallad_duck = MallardDuck()
rubber_duck = RubberDuck()
redhead_duck = RedHeadDuck()

print("### MALLAD DUCK ###")
mallad_duck.display()
mallad_duck.performFly()
mallad_duck.performQuack()


# class RubberDuck(Duck):
#     def __init__(self):
#         self.fly_behavior = FlyWithWings()
#         self.quack_behavior = Quack()

#     def display(self):
#         print("Rubber duck")


# class RedHeadDuck(Duck):
#     def __init__(self):
#         self.fly_behavior = FlyWithWings()
#         self.quack_behavior = MuteQuack()

#     def display(self):
#         print("Red head duck")
