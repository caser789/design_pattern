import os


class MoveFileCommand(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        os.rename(self.src, self.dest)

    def undo(self):
        os.rename(self.dest, self.src)

if __name__ == '__main__':
    undo_stack = []
    undo_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    undo_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    # foo.txt is now renamed to baz.txt

    undo_stack.pop().undo()
    # now it's bar.txt

    undo_stack.pop().undo()
    # now it's foo.txt
