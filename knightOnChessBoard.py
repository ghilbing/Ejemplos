def knight(A,B,C,D,E,F):
    #posible movements for a knight
    row = [2,2,-2,-2,1,1,-1,-1]
    col = [-1,1,1,-1,-2,2,2,-2]

    def valid(x, y):
        if x < 0 or y < 0 or x >= A or y >= B:
            return False
        return True

    
