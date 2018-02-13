def towerOfHanoi(n, source, helper, target):
    if n > 0:
        # move tower or size n-1 to helper
        towerOfHanoi(n - 1, source, helper, target)
        # move disk from source to target
        if source[0]:
            disk = source[0].pop()
            print "moving " + str(disk) + " from " + source[1] + " to " + target[1]

            target[0].append(disk)
        # move tower of size n-1 from helper to target
        towerOfHanoi(n - 1, helper, source, target)


source = ([5, 4, 3, 2, 1], "source")
target = ([], "target")
helper = ([], "helper")

towerOfHanoi(len(source[0]), source, target, helper)

print source, helper, target


def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
    #print(withPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


moveTower(4,"A","B","C")