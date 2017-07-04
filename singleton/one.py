class OneOnly(object):

    _singleton = None

    def __new__(cls, *args, **kw):
        if cls._singleton is None:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kw)
        return cls._singleton


# prefer module level variable

oo = OneOnly()
