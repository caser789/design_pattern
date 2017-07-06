from abc import ABCMeta, abstractmethod


class Compiler(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compile_and_run(self):
        self.collect_source()
        self.compile_to_object()
        self.run()


class iOSCompiler(Compiler):

    def collect_source(self):
        print 'Collecting Swift Source Code'

    def compile_to_object(self):
        print 'Compiling Swift code to LLVM bitcode'

    def run(self):
        print 'Program running on runtime environment'


ios = iOSCompiler()
ios.compile_and_run()
