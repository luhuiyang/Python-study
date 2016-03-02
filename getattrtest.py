class Test(object):
    def __init__(self, name):
        self.name = name

    def start(self):
        next = self.name
        print '-------------'
        then = getattr(self, next)
        next = then()

    def i_love_you(self):
        print 'i love you'

you = Test('i_love_you')
you.start()
