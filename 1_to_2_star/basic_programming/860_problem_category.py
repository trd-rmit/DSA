tc = int(input())

for _ in range(tc):
    r = int(input())
    if 1 <= r < 100:
        print("EASY")
    elif 100 <= r < 200:
        print("MEDIUM")
    elif 200 <= r <= 300:
        print("HARD")
