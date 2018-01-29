def findSubstring(s, words):
    from collections import deque, defaultdict, Counter
    s_len, word_len = len(s), len(words[0])
    word_len_total = len(words) * word_len
    count = Counter(words)
    footprint = defaultdict(deque)
    result = []
    for start in range(word_len):
        footprint.clear()
        end = start
        while start + word_len_total <= s_len:
            sub = s[end:end + word_len]
            end += word_len
            if sub in count:
                queue = footprint[sub]
                queue.append(end)
                while queue[0] < start:
                    queue.popleft()
                if len(queue) > count[sub]:
                    start = queue.popleft()
                if start + word_len_total == end:
                    result.append(start)
            else:
                start = end
    return result

#esta funcion anda con la de abajo
def testing(substring, lenword, counter):
    from collections import defaultdict
    i = 0
    seen = defaultdict(int)
    while i < len(substring):
        nextw = substring[i:i + lenword]
        if nextw not in counter or seen[nextw] == counter[nextw]:
            return False
        seen[nextw], i = seen[nextw] + 1, i + lenword
    return True


def anotherSolutionAccepted(self, A, B):
    from collections import Counter
    start = 0
    end = len(B) * len(B[0]) - 1
    counter = Counter(B)
    res = []
    while end < len(A):
        if self.testing(A[start:end + 1], len(B[0]), counter):
            res.append(start)
        start += 1
        end += 1

    return res


s = "barfoothefoobarman"
words = ["foo", "bar"]

A = "barfoothefoobarman"
B = ["foo", "bar"]

print findSubstring(s, words)
print anotherSolutionAccepted(self, A, B)
