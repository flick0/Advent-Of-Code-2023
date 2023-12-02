s = 0
with open("input") as f:
    raw = f.read()
    for line in raw.split("\n"):
        digits = [a for a in line if a.isdigit()]
        s += int(digits[0]+digits[-1])
print(s)
