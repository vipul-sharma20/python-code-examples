'''
Example of list data structure and methods of list objects
'''

def list_example():
    a = [1,2,4,5,6,7]
    
    # add item to the end of the list
    a.append(8)
    print a

    # insert item at a given position list.index(position, item)
    a.insert(2, 3)
    print a

    # remove the first item from the list whose value is x
    a.remove(8)
    print a

    # reverse the elements of the list in place
    b = a.reverse()
    print b

    # remove the item at the given position in the list
    temp = a.pop(0)
    print temp

    # sort the items of the list in place
    a.sort()
    print a

    # return the number of times an item appears in the list
    c = a.count(3)
    print c

    # returns index of the first item whose value is given as parameter
    index = a.index(5)
    print index

if __name__ == '__main__':
    list_example()
