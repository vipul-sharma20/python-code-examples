'''
Example of tuple
'''

a = (1, 2, 3, 4, 5)
b = (1, 'foo', 'bar', '2', True, 2.4)

# accessing values
print 'a[0]: ', a[0]

# updating tuple
# a[0] = 4 raises error as tuples are immutable
c = a + b # concatenation of a and b tuple

# delete tuple elements
# removing individual tuple elements is not possible
# but entire tuple can be removed
del c

# number of items in tuple
l = len(a)
print l

# convert list to tuple
c = tuple(a)

