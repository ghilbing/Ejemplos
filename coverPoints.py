def coverPoints(self, X,Y):
    steps = 0
    curX = X[0]
    curY = Y[0]
    for i in range(1, len(X)):
        steps += max(abs(curX - X[i]), abs(curY - Y[i]))
        curX = X[i]
        curY = Y[i]
    return steps


