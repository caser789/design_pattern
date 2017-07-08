class Publisher(object):
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print "Failed to add: {}".format(observer)

    def remove(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print "Failed to remove: {}".format(observer)

    def notify(self):
        [observer.notify(self) for observer in self.observers]


class DefaultFormatter(Publisher):

    def __init__(self, name):
        super(DefaultFormatter, self).__init__()
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print "Error {}".format(e)
        else:
            self.notify()


class HexFormatter(object):

    def notify(self, publisher):
        print "{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data))


class BinaryFormatter(object):

    def notify(self, publisher):
        print "{}: '{}' has now binary data = {}".format(type(self).__name__, publisher.name, bin(publisher.data))


if __name__ == '__main__':
    df = DefaultFormatter('test1')
    print df
    print '*' * 40

    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print df

    print '*' * 40
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print df

    print '*' * 40
    df.remove(hf)
    df.data = 40
    print df

    print '*' * 40
    df.remove(hf)
    df.add(bf)

    df.data = "hello"
    print df

    df.data = 14.3
    print df
