def longestCommonPrefix(elements):
    prefix = elements[0]
    for i in elements[1:]:
        while i.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
