def canReach(x1, y1, x2, y2):
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)

    if gcd(abs(x1), abs(y1)) == gcd(abs(x2), abs(y2)):
        return "Yes"
    else:
        return "No"

x1 = 1
y1 = 2
x2 = 2
y2 = 1

print canReach(x1, y1, x2, y2)

#this is working

while x2 >= x1 and y2 >= y1:
        if x1 == x2 and y1 == y2:
            return "Yes"
        if x2 > y2:
            x2 -= y2
        else:
            y2 -= x2
    return "No"
