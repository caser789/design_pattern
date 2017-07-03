class Image(object):
    def __init__(self, system):
        self.system = system

    def parse_file(self, fname):
        raise NotImplementedError


class JPEG(Image):

    def parse_file(self, fname):
        print 'jpeg'
        self.system.draw(1)


class PNG(Image):

    def parse_file(self, fname):
        print 'png'
        self.system.draw(1)


class OperatingSystem(object):

    def draw(self):
        raise NotImplementedError


class Windows(OperatingSystem):

    def draw(self, matrix):
        print 'draw in windows'


class Linux(OperatingSystem):
    def draw(self, matrix):
        print 'draw in linux'


def main():
    windows = Windows()
    png = PNG(windows)
    png.parse_file('a')


if __name__ == "__main__":
    main()
