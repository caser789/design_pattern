from abc import ABCMeta, abstractmethod


class You(object):

    def __init__(self):
        print "Let's buy the Denim shirt"
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print "You: Wow! Denium shirt is now mine :-)"
        else:
            print "You: I should earn more"


class Payment(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __has_funds(self):
        print "Bank: checking if {} has enough funds".format(self.__get_account())
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print "Bank: paying the merchant"
            return True
        else:
            print "Bank: sorry, not enough funds"
            return False


class DebitCard(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        num = raw_input('input the card number: \n')
        self.bank.set_card(num)
        return self.bank.do_pay()


if __name__ == "__main__":
    you = You()
    you.make_payment()
