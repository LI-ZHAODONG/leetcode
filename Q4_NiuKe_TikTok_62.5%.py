import sys

input_lines = sys.stdin.read().split('\n')
N = input_lines[0]
M = input_lines[1]
del input_lines[0]
del input_lines[0]

input_lines_new = []
for ele in input_lines:
    input_lines_new.append(list(ele))
space = []
for i in range(0, len(input_lines_new), 1):
    for y in range(0, len(input_lines_new[i]), 1):
        if input_lines_new[i][y] == " ":
            space.append(y)
    space.sort(reverse=True)
    for ind in space:
        del input_lines_new[i][ind]
    space.clear()
input_lines_new = [[int(value) for value in sublist] for sublist in input_lines_new]

for i in input_lines_new:
    if i[0] == 1:
        i.append(None)
        i.append(None)
    if i[0] == 0:
        i.append(None)
        i.append(None)
        i.append(None)
        i.append(None)
for i in range(0, len(input_lines_new), 1):
    del input_lines_new[i][0]

hold_x = 1
highest_rec_x = 0
hold_y = 1
highest_rec_y = 0
highest_rec = 0


# for x in range(0, len(input_lines_new), 1):
#     for i in range(0, len(input_lines_new[x]), 2):
#         j = i+1
#         if input_lines_new[x+1]
#         input_lines_new[x][i]
#         input_lines_new[x][j]

for i in range(0, len(input_lines_new) - 1, 1):
    if input_lines_new[i][0] == input_lines_new[i + 1][0] and input_lines_new[i][1] == input_lines_new[i + 1][1]:
        hold_x += 1
        if input_lines_new[i][0] == input_lines_new[i + 1][0] is None and input_lines_new[i][1] == input_lines_new[i + 1][1] is None:
            hold_x -= 1
    elif input_lines_new[i][0] == input_lines_new[i + 1][2] and input_lines_new[i][1] == input_lines_new[i + 1][3]:
        hold_x += 1
        if input_lines_new[i][0] == input_lines_new[i + 1][2] is None and input_lines_new[i][1] == input_lines_new[i + 1][3] is None:
            hold_x -= 1
    else:
        hold_x = 1
    if hold_x >= highest_rec_x:
        highest_rec_x = hold_x

    if input_lines_new[i][2] == input_lines_new[i + 1][2] and input_lines_new[i][3] == input_lines_new[i + 1][3]:
        hold_y += 1
        if input_lines_new[i][2] == input_lines_new[i + 1][2] is None and input_lines_new[i][3] == input_lines_new[i + 1][3] is None:
            hold_y -= 1
    elif input_lines_new[i][2] == input_lines_new[i + 1][0] and input_lines_new[i][3] == input_lines_new[i + 1][1]:
        hold_y += 1
        if input_lines_new[i][2] == input_lines_new[i + 1][0] is None and input_lines_new[i][3] == input_lines_new[i + 1][1] is None:
            hold_y -= 1
    else:
        hold_y = 1
    if hold_y >= highest_rec_y:
        highest_rec_y = hold_y

if highest_rec_x > highest_rec_y:
    print(highest_rec_x)
elif highest_rec_y > highest_rec_x:
    print(highest_rec_y)
else:
    print(highest_rec_x)

'''

1
8
2 1 1 2 2
2 1 1 1 4
2 1 1 2 2
2 2 2 1 4
0
0
1 1 1
1 1 1

1
3
2 0 0 1 1
2 0 1 3 3
2 3 3 4 4

'''
