def integerToRoman(number):

    numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", \
                   10: "X", 40: "XL", 50: "L", 90: "XC", \
                   100: "C", 400: "CD", 500: "D", 900: "CM", \
                   1000: "M"}
    keyset, result = sorted(numeral_map.keys()), []

    while 0 < number < 5000:
        for key in reversed(keyset):
            while number / key > 0:
                number -= key
                result += numeral_map[key]

    return "".join(result)


number = 3512


print integerToRoman(number)
