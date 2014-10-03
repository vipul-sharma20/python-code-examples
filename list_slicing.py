'''
Slicing operations on string, list and tuple
'''

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#a = 'abcdefghij'
#a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

# slicing from subscript 1 through subscript 2
# slice1 = 'bc'
slice1 = a[1:3]

# slicing from subscript 0 (empty begin index) through subscript 2
# slice2 = 'abc'
slice2 = a[:3]

# slicing from substring 1 through the last subscript (empty index)
# slice3 = 'bcdefghij'
slice3 = a[1:]

# slicing from subscript 0 through the last subscript
# slice4 = 'abcdefghij'
slice4 = a[:]

# slicing from the 2nd last subscript through the last subscript
# slice5 = 'ij'
slice5 = a[-2:]

# slicing from subscript 0 to 3rd last subscript
# slice6 = 'abcdefgh'
slice6 = a[:-2]
