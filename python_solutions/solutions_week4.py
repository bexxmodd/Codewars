# Simple Pig Latin (5 kyu)
def pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it('Hello world !'))   # elloHay orldway !
print(pig_it("O tempora o mores !")) # Oay emporatay oay oresmay !

# Good vs Evil (6 kyu)
def goodVsEvil(good, evil):
    # Convert strings into integers.
    goods = [int(g) for g in good.split()]
    evils = [int(e) for e in evil.split()]
    # Sum the weighted values for each race.
    alliance = sum([i * g for i, g in zip(goods, [1, 2, 3, 3, 4, 10])])
    horde = sum([i * e for i, e in zip(evils, [1, 2, 2, 2, 3, 5, 10])])
    # Declare the winner.
    if alliance > horde:
        return 'Battle Result: Good triumphs over Evil'
    elif alliance < horde:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'


print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))
