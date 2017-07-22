class EventManager(object):

    def __init__(self):
        print "Event Manager:: let me talk to the folks\n"

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier(object):

    def __init__(self):
        print "Arranging the hotel for marriage? --"

    def __is_available(self):
        print "Is the hotel free for the event on given day?"
        return True

    def book_hotel(self):
        if self.__is_available():
            print "registered the booking\n\n"


class Florist(object):

    def __init__(self):
        print "flower decorations for the event? --"

    def set_flower_requirements(self):
        print "Carnations, Roses and Lilies would be used for Decorations\n\n"


class Caterer(object):

    def __init__(self):
        print "food arrangements for the event --"

    def set_cuisine(self):
        print "chinese & continental cuisine to be served\n\n"


class Musician(object):

    def __init__(self):
        print "musical arrangements for the event --"

    def set_music_type(self):
        print "Jazz and Classical will be played"


class You(object):

    def __init__(self):
        print "You:: Whoa! Marriage Arrangements??!!"

    def ask_event_manager(self):
        print "You:: let's contact the event manager\n\n"
        em = EventManager()
        em.arrange()

    def __del__(self):
        print "You:: thanks to event manager, all preparations done! Phew!"

if __name__ == '__main__':
    you = You()
    you.ask_event_manager()
