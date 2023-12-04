with open("day3/input") as f:
    raw = f.read()

import numpy as np


lines = raw.split("\n")
m = np.matrix([list(l) for l in lines])

print(m)

line_y = len(lines)
line_x = len(lines[0])

repeat_check = []


def full_num(y, x):
    buf = ""
    offset_x = x
    while offset_x >= 0:
        if m[y, offset_x].isnumeric():
            if (y, offset_x) in repeat_check:
                return 0
            buf += m[y, offset_x]
            repeat_check.append((y, offset_x))
        else:
            break
        offset_x -= 1
    buf = buf[::-1]
    offset_x = x+1
    while offset_x < line_x:
        if m[y, offset_x].isnumeric():
            if (y, offset_x) in repeat_check:
                return 0
            buf += m[y, offset_x]
            repeat_check.append((y, offset_x))
        else:
            break
        offset_x += 1
    return int(buf or "0")

ans = 0

partnums = []
for y in range(line_y):
    nums = []
    for x in range(line_x):
        if not m[y, x].isnumeric() and m[y, x] != ".":
            print("symbol at", x, y, "is", m[y, x])

            # check top
            if y > 0:
                if m[y - 1, x].isnumeric():
                    nums.append(full_num(y - 1, x))
            
            # check bottom
            if y < line_y - 1:
                if m[y + 1, x].isnumeric():
                    nums.append(full_num(y + 1, x))
            
            # check left
            if x > 0:
                if m[y, x - 1].isnumeric():
                    nums.append(full_num(y, x - 1))
            
            # check right
            if x < line_x - 1:
                if m[y, x + 1].isnumeric():
                    nums.append(full_num(y, x + 1))
            
            # check top-left
            if y > 0 and x > 0:
                if m[y - 1, x - 1].isnumeric():
                    nums.append(full_num(y - 1, x - 1))
            
            # check top-right
            if y > 0 and x < line_x - 1:
                if m[y - 1, x + 1].isnumeric():
                    nums.append(full_num(y - 1, x + 1))

            # check bottom-left
            if y < line_y - 1 and x > 0:
                if m[y + 1, x - 1].isnumeric():
                    nums.append(full_num(y + 1, x - 1))

            # check bottom-right
            if y < line_y - 1 and x < line_x - 1:
                if m[y + 1, x + 1].isnumeric():
                    nums.append(full_num(y + 1, x + 1))

    print(m[y], nums)
    partnums.extend(nums)

print(sum(partnums))
            
                
