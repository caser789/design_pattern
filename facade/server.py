import abc
from enum import Enum

State = Enum("State", 'new running sleeping restart zombie')


class Server(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abc.abstractmethod
    def boot(self):
        pass

    @abc.abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):

    def __init__(self):
        """
        actions required for initializing the file system
        """
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print "booting the {}".format(self)
        """actions requred for booting the file server"""
        self.state = State.running

    def kill(self, restart=True):
        print "killing the {}".format(self)
        """actions required to kill the file server"""
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        """check validity of permissions, user rights, etc."""
        print "trying to create the file {} for user {} wiht permissions {}".format(name, user, permissions)


class ProcessServer(Server):

    def __init__(self):
        """actions required for initializing the process server"""
        self.name = "ProcessServer"
        self.state = State.new

    def boot(self):
        print "booting the {}".format(self)
        """actions requred for booting the process server"""
        self.state = State.running

    def kill(self, restart=True):
        print "killing the {}".format(self)
        """actions required to kill the process server"""
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        """check user rights, generate PID, etc."""
        print "trying to create process {} for user {}".format(name, user)


class OperatingSystem(object):
    """the facade"""

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file("foo", "hello", "-rw-r-r")
    os.create_process("bar", "ls /tmp")


if __name__ == "__main__":
    main()
