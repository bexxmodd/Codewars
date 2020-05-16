# Find the Parity Outlier
def find_outlier(integers):
    evens = [ n for n in integers if n % 2 == 0]
    odds = [n for n in integers if n % 2 != 0]
    return odds[0] if len(odds)<len(evens) else evens[0]

print('\nFind the Parity Outlier')
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([2017237, 9223811, 7987298, 7298917, 5446159, 7787747, -1159841, -3690463, 7787767, 5141195, -259751, -7235503]))

# Bouncing Balls
def bouncingBall(h, bounce, window):
    count = 0
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while (h * bounce) > window:
            count += 2
            h = h * bounce
        return count + 1
    else:
        return -1
print('\nBouncing Balls')
print(bouncingBall(3, 0.66, 1.5))
print(bouncingBall(30, 0.66, 1.5))
print(bouncingBall(3, 1, 1.5))


