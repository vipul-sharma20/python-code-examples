def tour(x, y, reached, possible_moves, a):
    print reached
    if len(reached) == 25:
        return True
    for pos in possible_moves:
        next_x = pos[0] + x
        next_y = pos[1] + y
        #print next_x, next_y
        check = False
        if next_x >= 0 and next_x < 5 and next_y >= 0 and next_y < 5 and [next_x, next_y] not in reached:
            reached.append([next_x, next_y])
            if tour(next_x, next_y, reached, possible_moves, a) == True:
                #print 'here'
                return True         
            else:
                reached.pop()
    return False


reached = [[0,0]]
location = [[0 for i in range(5)] for y in range(5)]
check = tour(0, 0, reached, [[2,1],[1,2],[-2,1],[-1,2],[-2,-1],[-1,-2],[1,-2],[2,-1]], 0)
if check:
    print 'path followed : ',
    print reached
    for elem in reached:
        location[elem[0]][elem[1]] += 1
    #print location
else:
    print 'Not possible'
#for elem in reached:
#    location[elem[0]][elem[1]] += 1

