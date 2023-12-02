s = 0

humandigits = {
    # "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

def find_num(buf:str):
    for a,k in humandigits.items():
        if buf.endswith(a):
            return humandigits[a]
        elif buf.endswith(k):
            return k
    return None
    
with open("input") as f:
    raw = f.read()
    for line in raw.split("\n"):
        buf = ""
        digits = ""
        for a in line:
            buf += a.lower()
            if find_num(buf):
                digits += find_num(buf)
        digits = digits[0] + digits[-1]
        print(digits)
        s += int(digits)
        
print(s)
