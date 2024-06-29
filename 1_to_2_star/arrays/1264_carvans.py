tc = int(input())

for _ in range(tc):
    no_cars = int(input())
    speeds = list(map(int, input().split()))
    hills = 1
    max_pos_speed = speeds[0]
    if no_cars == 1:
        hills = 1
    else:
        for i in range(1, no_cars):
            if speeds[i] <= max_pos_speed:
                hills += 1
                max_pos_speed = speeds[i]
    print(hills)
