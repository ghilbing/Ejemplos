source = [4, 2, 1, 10, 5, 3, 100]


def selectionSort(source):

    for i in range(len(source)):
        for j in range(i, len(source)):
            if source[i] > source[j]:
                source[i], source[j] = source[j], source[i]

    print source


print selectionSort(source)
