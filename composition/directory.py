class Component(object):

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def get_child(self, index):
        pass

    def operation(self):
        pass


class Leaf(Component):

    def add(self, component):
        print 'leaf do no have add'

    def remove(self, component):
        print 'leaf do no have remove'

    def get_child(self, index):
        print 'leaf do no have child'

    def operation(self):
        pass


class Composite(Component):

    def __init__(self):
        self.components = list()

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def get_child(self, index):
        return self.components[index]

    def operation(self):
        for component in self.components:
            component.operation()
