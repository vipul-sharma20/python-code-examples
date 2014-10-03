def decorator(args):
    print 'inside decorator method'

@decorator
def function(arg):
    print 'Return'

if __name__ == '__main__':
    function()
# Above code eqivalent to:
"""
def function(arg):
    return "Return"
function=decorator(function)
"""

