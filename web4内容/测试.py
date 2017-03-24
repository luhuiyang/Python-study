class Model(object):
    def __init__(self):
        self.time = '123'
        self.ut = '111'
        self.form = {
            'a': 5,
            1: 3,
        }

a = Model()

b = a.__dict__
print(a)
print(b)