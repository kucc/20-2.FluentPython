
class ndarray:
    
    def __init__(self, lst):
        self.lst = lst
        self.size = len(lst)
        self.shape = (self.size,)

    def __repr__(self):
        return 'array(%s)' % repr(self.lst)

    def __str__(self):
        return repr(self.lst)
