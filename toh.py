def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        print 'n-1'
        moveDisk(fromPole,toPole)
        print 'n'
        moveTower(height-1,withPole,toPole,fromPole)
        print 'last'
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")
