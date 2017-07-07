from abc import ABCMeta, abstractmethod


class AbstractClass(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print "Defining the algorithm. Operation1 follows Operation2"
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):

    def operation1(self):
        print "My Concrete Operation1"

    def operation2(self):
        print "My Concrete Operation2"


class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()


client = Client()
client.main()