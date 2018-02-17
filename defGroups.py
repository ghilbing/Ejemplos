def getTheGroups(n, queryType, students1, students2):
    if n == 0 or len(queryType) == 0 or len(students1) == 0 or len(students2) == 0:
        return [0]
    friends = [n]
    count = [n]
    lista = []
    res = []

    def friendship(i, friends):
        while i != friends[i]:
            friends[i] = friends[friends[i]]
            i = friends[i]
        return i

    for i in range(len(friends)):
        friends[i] = i

    for j in range(len(count)):
        count[i] = 1
    for i in range(len(queryType)):
        student1 = students1[i]
        student2 = students2[i]
        if queryType[i] == "Friend":
            var1 = friendship(student1, friends)
            var2 = friendship(student2, friends)

            if (var1 != var2):
                friends[var1] = var2
                count[var2] += count[var1]
        else:
            var1 = friendship(student1, friends)
            var2 = friendship(student2, friends)
            if var1 != var2:
                lista.append(count[var1] + count[var2])
            else:
                lista.append(count[var1])
    for i in range(len(lista)):
        res[i] = lista.pop(i)

n = 3
queryType = [Friend, Total]
students1 = [1,2]
students2 = [2,3]





























