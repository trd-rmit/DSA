t = int(input())

while t > 0:
    x = input()
    y = input()
    # Your code goes here
    for i, j in zip(x, y):
        if i != j and (i != '?' and j != '?'):
            print("No")
            break
    else:
        print("Yes")
    t -= 1
