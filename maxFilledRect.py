def maximalFilledRectangle(matrix, findVal):
    """return (x,y), (w,h) of max rect"""
    maxArea, maxX, maxY, maxW, maxH = 0,0,0,0,0
    maxRow = len(matrix)
    maxCol = len(matrix[0])
    # For every row in the given 2D matrix, it is a "Largest Rectangle in
    # Histogram" problem, which is the sub-problem.
    lookupTable = [0 for _ in range(maxCol)]
    for row in range(maxRow):
        for col in range(maxCol):
            if matrix[row][col] == findVal:
                lookupTable[col] += 1
            else:
                lookupTable[col] = 0
        curArea, curW, curH, curCol = maximalRectangleInHistogram(lookupTable)
        if curArea > maxArea:
            maxArea = curArea
            maxY = row
            maxX = curCol
            maxW = curW
            maxH = curH
    return (maxX-1, maxY), (maxW, maxH)

def maximalRectangleInHistogram(histogram):
    posStack = []
    i = 0
    maxArea, maxW, maxH, maxCol = 0,0,0,0
    while i < len(histogram):
        if len(posStack) == 0 or histogram[i] > histogram[posStack[-1]]:
            posStack.append(i)
            i += 1
        else:
            curr = posStack.pop()
            width = i if len(posStack) == 0\
                else i - posStack[-1] - 1
            curArea = width * histogram[curr]
            if curArea > maxArea:
                maxArea = curArea
                maxW = width
                maxH = histogram[curr]
                maxCol = i
    while posStack:
        curr = posStack.pop()
        width = i if len(posStack) == 0\
            else len(histogram) - posStack[-1] - 1
        curArea = width * histogram[curr]
        if curArea > maxArea:
            maxArea = curArea
            maxW = width
            maxH = histogram[curr]
            maxCol = i
    return maxArea, maxW, maxH, maxCol
    
#examples of usage:  

#print maximalFilledRectangle([
#  [0,0,0,0,0,0,0,0],
#  [0,0,0,1,1,1,1,0],
#  [0,0,1,1,1,1,1,0],
#  [0,0,1,1,1,1,1,0],
#  [0,0,0,0,0,0,0,0]], 1)
#  #will return (6,3),(4,3) - bottom-right corner and size of rectange of 1's

#print maximalFilledRectangle([[1]], 1) #(0,0),(1,1)
#print maximalFilledRectangle([[0]], 1) #(-1,0),(0,0) - no real rect
#print maximalFilledRectangle([[0,1],[0,1]], 1) #(1, 1), (1, 2)
#print maximalFilledRectangle([[0,1,1],[0,1,1], [0,0,0]], 1) #(2, 1), (2, 2)