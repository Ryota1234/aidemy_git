import random

with open("./hyakunin.txt", encoding="utf-8") as f:
    wakas = [f.strip() for f.readlines()]

print("今日の一句" + wakas[random.randrange(len(wakas))])