# Slower
def romanToInt(s):
    # strip for remove things
    # split for make things into array
    s = list(s)
    sum = 0
    d = []
    for i in range(0, len(s) - 1, 1):
        if s[i] == "I" and s[i + 1] == "V":
            sum += 4
            d.append(i)
            d.append(i + 1)
        elif s[i] == "I" and s[i + 1] == "X":
            sum += 9
            d.append(i)
            d.append(i + 1)
        elif s[i] == "X" and s[i + 1] == "L":
            sum += 40
            d.append(i)
            d.append(i + 1)
        elif s[i] == "X" and s[i + 1] == "C":
            sum += 90
            d.append(i)
            d.append(i + 1)
        elif s[i] == "C" and s[i + 1] == "D":
            sum += 400
            d.append(i)
            d.append(i + 1)
        elif s[i] == "C" and s[i + 1] == "M":
            sum += 900
            d.append(i)
            d.append(i + 1)
    d.sort(reverse=True)
    for i in range(0, len(d), 1):
        del s[d[i]]

    for i in range(0, len(s), 1):
        if s[i] == "I":
            sum += 1
        if s[i] == "V":
            sum += 5
        if s[i] == "X":
            sum += 10
        if s[i] == "L":
            sum += 50
        if s[i] == "C":
            sum += 100
        if s[i] == "D":
            sum += 500
        if s[i] == "M":
            sum += 1000

    return sum


# Faster
def romanToInt_(s):
    translate = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum_ = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        sum_ += translate[char]
    return sum_


print(romanToInt_("III"))
