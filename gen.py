'''
Example of generator function
'''

# genertator function
def generator(n):
    i = 1
    while i <= n:
        yield i  # used as return, except the function will return a generator
        i += 1

gen = generator(3)  # create a generator object 

# returning yielded values by calling next method on generator object
print gen.next()
print gen.next()
print gen.next()
print gen.next()
