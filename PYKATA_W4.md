_In this section I will be copying the Codewars exercises and aranging them by date within month. Each of the exercise will have it's difficulty assignt and as soon as the exercise is solved it will have check mark. In another file, I will post all the solved exercises which will be linked by the exercise name_

----------
# May
### Total Exercises Completed = 1

### Total Exercises Attempted = 1

-----------
## Week 3: 05-24-2020 to 05-30-2020

- [x] **Simple Pig Latin (5 kyu)**

Description:

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

_Examples:_

`pig_it('Pig latin is cool') # igPay atinlay siay oolcay`
`pig_it('Hello world !')     # elloHay orldway !`

-----------
- [x] **Good Vs Evil (6 kyu)**

## Description
Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races will be involved. Each race has a certain worth when battling against others. On the good ise we have the following races, with their associated worth:
* Hobbits: 1
* Men: 2
* Elves: 3
* Dwarves: 3
* Eagles: 4
* Wizards: 10

On the side of evil we have:
* Orcs: 1
* Men: 2
* Wargs: 2
* Goblins: 2
* Uruk Hai: 3
* Trolls: 5
* Wizards: 10

Add up the worth of the side of good and compare it with the worth of the evil side, the side with the larger worth will win. Thus, given the count of each of the races on each side and determine which side wins.

Input:
The function will be given two parameters. Each parameter will be a string of multiple integers separated by a single space. Each string will contain the count of each race on the side of good and evil.

The first parameter will contain the count of each race on the side of good in the following order:
* Hobbits, Men, Elves, Dwarves, Eagles, Wizards.

The second parameter will contain the count of each race on the evil side in the following order:
* Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.

Output:
Return `"Battle Result: Good triumphs over Evil"` if good wins, `"Battle Result: Evil eradicates all trace of Good"` if evil wins, or `"Battle Result: No victor on this battle field"` if it ends in a tie.
