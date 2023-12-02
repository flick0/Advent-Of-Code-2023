s = 0
with open("1.txt") as f:
    raw = f.read()
    for line in raw.split("\n"):
        digits = [a for a in line if a.isdigit()]
        print(int("".join(digits)))
        s += int(digits[0]+digits[-1])
print("==")
print(s)
