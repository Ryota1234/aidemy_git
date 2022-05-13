import random

with open("./hyakunin.txt", encoding="utf-8") as f:
    wakas = [s.strip() for f.readlines()]

print(wakas[random.randrange(len(wakas))])