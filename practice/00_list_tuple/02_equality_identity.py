
# mutability of list
lst = [1, 2, 3]

print('== the original list ==')
print('lst: ', lst)
print('id(lst): ', id(lst), '\n')

lst += [4] # lst.append(4)
print('== the list after append ==')
print('lst: ', lst)
print('id(lst): ', id(lst), '\n')  # not changed


# mutability of list
tup = (1, 2, 3)

print('== the original tuple ==')
print('tup: ', tup)
print('id(tup): ', id(tup), '\n')

tup += (4,)
print('== the tuple after append ==')
print('tup: ', tup)
print('id(tup): ', id(tup), '\n')  # not changed

