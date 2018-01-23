def justifiedText(A, B):
    n = len(A)
    if n == 0:
        return []
    ret = []
    i = 0
    while i < n:
        line = ""
        line_words = []
        length = 0
        k = i
        while k < n:
            if length + len(line_words) + len(A[k]) <= B:
                line_words.append(A[k])
                length += len(A[k])
            else:
                break
            k += 1
        i = k
        # print length, line_words, k
        if k < n:
            if len(line_words) > 1:
                space = (B - length) / (len(line_words) - 1)
                remain = (B - length) % (len(line_words) - 1)
                line += line_words[0]
                line += " " * space
                if remain > 0:
                    line += " "
                remain -= 1
                for j in range(1, len(line_words) - 1):
                    line += line_words[j]
                    line += " " * space
                    if remain > 0:
                        line += " "
                    remain -= 1
                if len(line_words) > 1:
                    line += line_words[-1]
            else:
                line += line_words[0]
                line += " " * (B - len(line))
        else:
            line += line_words[0]
            for j in range(1, len(line_words)):
                line += " " + line_words[j]
            line += " " * (B - len(line))
        ret.append(line)
    return ret

A = ["This", "is", "an", "example", "of", "text", "justification"]
#A = [ "" ]
B = 16
words = ["This", "is", "an", "example", "of", "text", "justification"]
L = 16


def justifyText(words, L):
    firstWord = 0
    numWords = 0
    caractersInLine = 0
    solution = []

    for i in range(0, len(words)):
        if caractersInLine + numWords + len(words[i])>L:
            line = []
            if numWords > 1:
                spaces = (L-caractersInLine) // (numWords-1)
                extraspaces = (L-caractersInLine) % (numWords-1)
            for j in range(firstWord, i):
                line.append(words[j])
                if j == i-1:
                    break
                for n in range(0, spaces):
                    line.append(' ')
                if j - firstWord < extraspaces:
                    line.append(' ')
            if numWords == 1:
                for n in range(len(words[firstWord]), L):
                    line.append(' ')
            solution.append(''.join(line))
            firstWord = i
            numWords = 0
            caractersInLine = 0
        numWords +=1
        caractersInLine += len(words[i])
    line = []
    if firstWord == 0 or firstWord < len(words):
        line = []
        for j in range(firstWord, len(words)):
            line.append(words[j])
            if j == len(words)-1:
                break
            line.append(' ')
        for n in range(len(''.join(line)), L):
            line.append(' ')
        solution.append(''.join(line))
    return solution


def fullJustify(words, L):
    res = []
    cur = []
    num_of_letters = 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > L:
            for i in range(L - num_of_letters):
                cur[i%(len(cur)-1 or 1)] +=' '
            res.append(''.join(cur))
            cur = []
            num_of_letters = 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(L)]

def fullyJustify(words, L):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > L:
            if len(cur) == 1:
                res.append(cur[0] + ' ' * (L - num_of_letters))
            else:
                num_spaces = L - num_of_letters
                space_between_words, num_extra_spaces = divmod(num_spaces, len(cur) - 1)
                for i in range(num_extra_spaces):
                    cur[i] += ' '
                res.append((' ' * space_between_words).join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    res.append(' '.join(cur) + ' ' * (L - num_of_letters - len(cur) + 1))
    return res


def fj(words, L):
    res = []
    line = []
    num_of_letters = 0

    for w in words:
        if num_of_letters + len(line) + len(w) > L:
            if len(line) == 1:
                res.append(line[0] + ' ' * (L - num_of_letters))
            else:
                num_of_spaces = L - num_of_letters
                spaces_btw_words, extra_spaces = divmod(num_of_spaces, len(line)-1)
                for i in range(extra_spaces):
                    line[i] += ' '
                res.append((' ' * spaces_btw_words).join(line))
            line = []
            num_of_letters = 0
        num_of_letters += len(w)
        line += [w]
    res.append(''.join(line) + ' ' * (L - num_of_letters - len(line)+ 1))
    return res


print justifiedText(A, B)
print justifyText(words,L)
print fullJustify(words, L)
print fullyJustify(words, L)
print fj(words, L)