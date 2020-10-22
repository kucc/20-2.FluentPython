
# tuple: immutable
# list: mutable

tup = (1, 2, [30, 40])
print(tup)


try:
    tup[2] += [50, 60] # error: tuple is immutable
except:
    # will be executed when error occurred.
    print(tup)  # (1, 2, [30, 40, 50, 60])
