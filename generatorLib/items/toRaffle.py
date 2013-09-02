import sys

rarityToNum = dict()
with open("rarityLevels.txt") as f:
    for line in f:
        rarity, value = line.split(":")
        rarity = rarity.strip()
        value = value.strip()
        rarityToNum[rarity] = value

with open(sys.argv[1]) as inFile:
    for line in inFile:
        item, rarity = line.split(":")
        item = item.strip()
        rarity = rarity.strip().lower()
        print item + ":" + rarityToNum[rarity]
