def findOpenEntry(carWidth, parkingLot):
    top = []
    bottom = []
    front = []
    back = []

    # loop over the lot
    for i in range(0, len(parkingLot) - carWidth + 1):
        frontCol = []
        backCol = []
        # front and back
        for j in range(i, i+carWidth):
            frontCol.append(parkingLot[j][0])
            backCol.append(parkingLot[j][-1])

        if not any(frontCol):
            # possible, add the entry index
            front.append((i,0))
        if not any(backCol):
            back.append((i,-1))

    # again, but this time the top and bottom
    for i in range(0, len(parkingLot[0])-carWidth+1):
        if not any(parkingLot[0][i:i+carWidth]):
            top.append((0,i))
        if not any(parkingLot[-1][i:i+carWidth]):
            bottom.append((-1,i))

    return top,bottom,front,back


def parkingSpot(carDimensions, parkingLot, luckySpot):
    # find possible openings in the lot for the car
    (top,bottom,front,back) = findOpenEntry(carDimensions[1],parkingLot)

    # no possible entry points
    if not sum(map(len,[top,bottom,front,back])):
        return False

    # otherwise, loop over the possible entry points to see if the spot is open
    cantFit = False
    for entry in top:
        # from top to bottom, see if the car fits for this entry point
        for i in range(0,len(parkingLot) - carDimensions[0] + 1):
            if cantFit:
                break
            # for all the rows across the length of the car, check each column
            for j in range(entry[1],entry[1] + carDimensions[1]):
                if cantFit:
                    break
                col = [row[j] for row in parkingLot[i:i+carDimensions[0]]]
                if any(col):
                    cantFit = True
                    break
            # see if we are at the lucky spot
            if not cantFit:
                if luckySpot[0] == i and luckySpot[2] == i + carDimensions[0] - 1 and \
                        luckySpot[3] == entry[1] and luckySpot[1] == entry[1] + carDimensions[1] -1:
                        return True

    cantFit = False
    for entry in bottom:
        # from top to bottom, see if the car fits for this entry point
        for i in range(len(parkingLot)-1,carDimensions[0]-1,-1):
            if cantFit:
                break
            # for all the rows across the length of the car, check each column
            for j in range(entry[1], entry[1] + carDimensions[1]):
                if cantFit:
                    break
                col = [row[j] for row in parkingLot[i:i - carDimensions[0]:-1]]
                if any(col):
                    cantFit = True
                    break
            # see if we are at the lucky spot
            if not cantFit:
                if luckySpot[2] == i and luckySpot[0] == i - carDimensions[0] + 1 and \
                        luckySpot[1] == entry[1] and luckySpot[3] == entry[1] + carDimensions[1] - 1:
                        return True

    cantFit = False
    for entry in front:
        for i in range(0,len(parkingLot[0])-carDimensions[0]+1):
            if cantFit:
                break
            for j in range(entry[0],entry[0] + carDimensions[1]):
                if cantFit:
                    break
                if any(parkingLot[j][i:i+carDimensions[0]]):
                    cantFit = True
                    break
            if not cantFit:
                if luckySpot[0] == i and luckySpot[2] == i + carDimensions[1] -1 and \
                        luckySpot[1] == entry[0] and luckySpot[3] == entry[0] + carDimensions[0] -1:
                        return True

    cantFit = False
    for entry in back:
        for i in range(len(parkingLot[0])-1,carDimensions[0]-1,-1):
            if cantFit:
                break
            for j in range(entry[0],entry[0] - carDimensions[1],-1):
                if cantFit:
                    break
                if any(parkingLot[j][i:i-carDimensions[0]:-1]):
                    cantFit = True
                    break
            if not cantFit:
                if luckySpot[3] == i and luckySpot[1] == i - carDimensions[0] + 1 and \
                        luckySpot[0] == entry[0] and luckySpot[2] == entry[0] + carDimensions[1] -1:
                        return True
    return False

print parkingSpot([7,2],
                  [[0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]],
            [1,1,2,7])
print parkingSpot([3,2],
                  [[1, 0, 1, 0, 1, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1]],
                  [1,1,2,3])
print parkingSpot([2,1],
                  [[1, 0, 1],
                   [1, 0, 1],
                   [1, 1, 1]],
                  [0,1,1,1])

print parkingSpot([7,2],
                  [[0, 1, 0],
                   [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]],
                  [1,0,7,1])

print parkingSpot([2,1],
                  [[1, 1, 1, 1],
                   [1, 0, 0, 0],
                   [1, 0, 1, 0]],
                  [1,2,1,3])
