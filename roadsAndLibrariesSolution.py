def solve(A, B, C, D ,E, F):
    def explore(city):
        global cost
        c = roads[city]
        for j in c:
            if cities[i] != 1:
                cities[i] = 1
                cost += c_road
                explore(city)

A = 3
B = 3
C = 2
D = 1
E = [[1,2],[3,1],[2,3]]

