
lst1 = [1, [11, 12, 13], (21, 22, 23)]
lst2 = list(lst1) # copy lst1

print('== copy lst1 to lst2 ==')
print('lst1(id = %d): ' % id(lst1), lst1)
print('lst2(id = %d): ' % id(lst2), lst2, '\n\n')


print('== the id of element? ==')
print('1. lst1[1] vs lst2[1] (list)')
print('lst1[1] (id = %d): ' % id(lst1[1]), lst1[1])
print('lst2[1] (id = %d): ' % id(lst2[1]), lst2[1], '\n')

print('2. lst1[2] vs lst2[2] (tuple)')
print('lst1[2] (id = %d): ' % id(lst1[2]), lst1[2])
print('lst2[2] (id = %d): ' % id(lst2[2]), lst2[2], '\n\n')

lst1[1].append(14)
print('== after append to lst1[1] ==')
print('lst1(id = %d): ' % id(lst1), lst1)
print('lst2(id = %d): ' % id(lst2), lst2)
print('lst1[1] (id = %d): ' % id(lst1[1]), lst1[1])
print('lst2[1] (id = %d): ' % id(lst2[1]), lst2[1], '\n\n')

lst1[2] += (24, )
print('== after append to lst1[2] ==')
print('lst1(id = %d): ' % id(lst1), lst1)
print('lst2(id = %d): ' % id(lst2), lst2)
print('lst1[2] (id = %d): ' % id(lst1[2]), lst1[2])
print('lst2[2] (id = %d): ' % id(lst2[2]), lst2[2])
