import sys

input_line = sys.stdin.read().split()
input_lines = []
for x in input_line:
    input_lines.append(int(x))

count_dict = {}


def times(input_l):
    for value in input_l:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict


count_dictionary = times(input_lines)
only = 0
count = 0
for key, val in count_dictionary.items():
    if val == 1:
        only = key
        count += 1
if count == 1:
    print(only)

A = []
for add in range(1, 10, 1):
    input_lines.append(add)
    count_dictionary = times(input_lines)
    for k, _ in count_dictionary.items():
        A.append(k)
    for QT in range(0, len(A), 1):
        if count_dictionary[A[QT]] >= 2:
            count_dictionary[A[QT]] -= 2
            for key, v in count_dictionary.items():
                while (key + 1 and key + 2 in count_dictionary) and v > 0 and count_dictionary[key + 1] > 0 and count_dictionary[key + 2] > 0:
                    v -= 1
                    count_dictionary[key + 1] -= 1
                    count_dictionary[key + 2] -= 1
    if all(value == 0 for value in count_dictionary.values()):
        print(add)

# 输入例子：
# 1 1 1 1 2 2 3 3 5 6 7 8 9
# 输出例子：
# 4 7
# 例子说明：
# 用1做雀头，组123,123,567或456,789的四个顺子

# while True:
#     if True:
#         input_lines.append(1)
#
#     if True:
#         input_lines.append(2)
#
#     if True:
#         input_lines.append(3)
#
#     if True:
#         input_lines.append(4)
#
#     if True:
#         input_lines.append(5)
#
#     if True:
#         input_lines.append(6)
#
#     if True:
#         input_lines.append(7)
#
#     if True:
#         input_lines.append(8)
#
#     if True:
#         input_lines.append(9)
