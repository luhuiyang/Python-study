class Dict(object):
    def __init__(self):
        self.name = 'Just a test.'

    def open(self):
        print self.name + ' and so exciting '

mydict = Dict()

mydict.__dict__
dir(Dict)

mydict.open()
