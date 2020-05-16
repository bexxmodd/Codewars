# Find the Parity Outlier (6 kyu)
def find_outlier(integers):
    evens = [ n for n in integers if n % 2 == 0]
    odds = [n for n in integers if n % 2 != 0]
    return odds[0] if len(odds)<len(evens) else evens[0]

print('\n** Find the Parity Outlier => 6 kyu! **')
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([2017237, 9223811, 7987298, 7298917, 5446159, 7787747, -1159841, -3690463, 7787767, 5141195, -259751, -7235503]))


# Bouncing Balls (6 kyu)
def bouncingBall(h, bounce, window):
    count = 0
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while (h * bounce) > window:
            count += 2
            h = h * bounce
        return count + 1
    else:
        return -1
print('\n** Bouncing Balls => 6 kyu! **')
print(bouncingBall(3, 0.66, 1.5))
print(bouncingBall(30, 0.66, 1.5))
print(bouncingBall(3, 1, 1.5))


# Scramblies (5 kyu)
def scramble(s1, s2):
    check = all(i in sorted(s1) for i in sorted(s2))
    return True if check is True else False

print('\n** Scranblies => 5 kyu! **')
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))




