quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself',
    'Behind a success man is an exhausted woman',
    'Black holes realy sucks',
    'Facts are stubborn things'
)


class QuoteModel(object):

    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError:
            value = 'Not Found'
        return value


class QuoteTerminalView(object):

    def show(self, quote):
        print "And the quote is {}".format(quote)

    def error(self, msg):
        print "error: {}".format(msg)

    def select_quote(self):
        return raw_input('which quote number? \n')


class QuoteTerminalControler(object):

    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
            except ValueError:
                self.view.error('incorrect index: {}'.format(n))
            else:
                valid_input = True
            quote = self.model.get_quote(n)
            self.view.show(quote)


if __name__ == "__main__":
    controller = QuoteTerminalControler()
    while True:
        controller.run()
