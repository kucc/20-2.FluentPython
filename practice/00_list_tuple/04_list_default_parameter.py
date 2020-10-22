class myarray:
    def __init__(self, lst=[]):
        self.lst = lst
        
    def add(self, value):
        self.lst.append(value)
        
    def remove(self, value):
        self.lst.remove(value)
        
    def print(self):
        print('myarray(%s)' % str(self.lst))

arr1 = myarray([1, 2, 3])
arr1.print()

arr2 = myarray()
arr2.add(10)
arr2.print()

arr3 = myarray()
arr3.print()

