'''
Iterating over iterable objects:
list, string, dictionary, text file
'''

# iterating over a list
test_list = [1, 2, 3, 4]
for i in test_list:
    print i

# iterating over characters of string
test_string = 'python'
for c in test_string:
    print c

# iterating over dictionary keys
test_dict = {'x': 1, 'y': 2}
for k in test_dict:
    print k

# iterating over a text file
for line in open('test.txt'):
    print line
