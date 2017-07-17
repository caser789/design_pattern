class Actor(object):

    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print "{} is occupied with current movie".format(type(self).__name__)

    def available(self):
        self.is_busy = False
        print "{} is free for the movie".format(type(self).__name__)

    def get_status(self):
        return self.is_busy


class Agent(object):

    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == "__main__":
    a = Agent()
    a.work()
