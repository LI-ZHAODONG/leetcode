import re
import sys

input_lines = sys.stdin.read().splitlines()

N = int(input_lines[0])

pattern = r'^(\w)\1(\w)(?!\1)\2$'

del input_lines[0]

for req in input_lines:
    req_list = list(req)
    length = len(req_list)
    index = []
    count = 0
    temp = 0
    for y in range(0, length-2, 1):
        if req_list[y] == req_list[y+1] == req_list[y+2]:
            index.append(y)
        index.sort(reverse=True)
    for ind in index:
        del req_list[ind]

    while True:
        for x in range(0, len(req_list)-3, 1):
            if (re.match(pattern, (req_list[x] + req_list[x + 1] + req_list[x + 2] + req_list[x + 3])) is not None) is True:
                del req_list[x + 3]
                count += 1
                break
        if count > temp:
            temp = count
        else:
            break

    res = "".join(req_list)
    print(res)