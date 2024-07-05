# This one too slow
def rec(x):
    A = []
    judge = True
    if x >= 0:
        while True:
            digit = x % 10
            x = int(x / 10)
            A.append(digit)
            if x == 0:
                break
        if len(A) % 2 != 0:
            del A[int(len(A) / 2)]
        for i in range(0, int(len(A) / 2), 1):
            if A[i] != A[len(A) - 1 - i]:
                judge = False
    else:
        judge = False
    return judge


def pal(x):
    if x < 0:
        return False
    reverse = 0
    x_copy = x
    while x != 0:
        reverse = (10 * reverse) + (x % 10)
        x //= 10
    return reverse == x_copy


num = pal(12321)
print(num)
