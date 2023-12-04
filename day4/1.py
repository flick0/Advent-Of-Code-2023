with open("day4/input") as f:
    raw = f.read()

def get_winning(cards, winning):
    # print(f"{winning}")
    for card in cards:
        if card in winning:
            # print("found", card)
            yield card
        
            
ans = 0

for line in raw.split("\n"):
    name,raw = line.split(":")
    _cards,_winning = raw.split("|")
    cards = map(int, _cards.split())
    winning = map(int, _winning.split())

    points = 0
    print(name,":", end=" ")
    for card in get_winning(list(cards), list(winning)):
        print(card, end=" ")
        if not points: points = 1
        points *= 2
    print(f":: {points//2}")

    ans += points//2

print(ans)
        