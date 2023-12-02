with open("3.txt") as f:
    raw = f.read()

games = []

actual_game = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

s = 0

def check_game(game):
    for color in actual_game:
        if actual_game[color] < game[color]:
            return False
    return True


for line in raw.split("\n"):
    game_index = int(line.split(":")[0].split(" ")[1].strip())

    game = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    turns = line.split(":")[1].strip()
    cubes = map(lambda x: x.strip(),turns.replace(";",",").split(","))
    for cube in cubes:
        number, color = cube.split(" ")
        if game[color] < (num:=int(number)):
            game[color] = num
    
    if check_game(game):
        s += game_index

print(s)