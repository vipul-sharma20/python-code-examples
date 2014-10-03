'''
Example of dictionary data structure by implementing a phonebook 
'''
# make a phonebook
phonebook = {
            "saransh" : 8827931450,
            "vipul" : 8127455455,
            "" : 9793755111,
            }

# add a person 'bazz' to the phonebook
phonebook['bazz'] = 8010303540

# removing entries from phonebook
del phonebook['foo']

# dict.has_key(key) returns true of dictionary has 'key' in it
if phonebook.has_key('lorem'):
    print "lorem is listed in the phonebook. Number: ",
    print phonebook['lorem']
else:
    print "lorem is not listed in the phonebook."

# dict.keys() returns a list of all the names of the keys
keys = phonebook.keys()
print keys

# dict.values() returns list of all the values in a dictionary
values = phonebook.values()
print values

# returns number of entries in a dictionary
count = len(phonebook)
print count

# iterating over dictionary
for name, number in phonebook.iteritems():
    print name, number
