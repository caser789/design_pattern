from abc import abstractmethod, ABCMeta


class State(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):

    def handle(self):
        print 'a'


class ConcreteStateB(State):

    def handle(self):
        print 'b'


class Context(State):

    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()
