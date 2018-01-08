def reverse_a_string_more_slowly(a_string):
    # new_strings = []
    # index = len(a_string)
    # while index:
    #     index -= 1
    #     new_strings.append(a_string[index])
    # return ''.join(new_strings)
    return a_string[-1::-1]

a_string = "Hello"
print reverse_a_string_more_slowly(a_string)