# this one takes like 10 mins to finish :skull:

with open("day4/input") as f:
    raw = f.read()

def get_winning(cards, winning):
    for card in cards:
        if card in winning:
            yield card
    
_cards = []

for line in raw.split("\n"):
    name,raw = line.split(":")
    _numbers,_winning = raw.split("|")
    numbers = list(map(int, _numbers.split()))
    winning = list(map(int, _winning.split()))
    _cards.append([name,numbers,winning])

winmap = {}

for card in _cards:
    name,numbers,winning = card
    cardnum = int(name.split()[1])
    wins = list(get_winning(numbers, winning))
    cards_to_win = []

    w=cardnum
    for win in wins:
        w+=1
        cards_to_win.append(w)
    
    winmap[cardnum] = cards_to_win

cards = [*winmap.keys()]

t=0
while True:
    cards.extend(winmap[cards[t]])
    print(f"{cards[t]} won {winmap[cards[t]]}")
    t+=1
    if t >= len(cards):
        break
print(len(cards))