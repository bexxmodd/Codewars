_In this section I will be copying the Codewars exercises and aranging them by date within month. Each of the exercise will have it's difficulty assignt and as soon as the exercise is solved it will have check mark. In another file, I will post all the solved exercises which will be linked by the exercise name_

----------
# May
### Total Exercises Completed = 4

### Total Exercises Attempted = 4

## Week 3 05-17-2020 to 05-23-2020

- [X] **Find the Parity Outlier (6 kyu)**

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

Examples

`[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)`

`[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)`

-------
- [X] **Bouncing Balls (6 kyu)**

A child is playing with a ball on the nth floor of a tall building. The height of this floor, _h_, is known.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

### Three conditions must be met for a valid experiment:
* Float parameter "h" in meters must be greater than 0
* Float parameter "bounce" must be greater than 0 and less than 1
* Float parameter "window" must be less than h.

**If all three conditions above are fulfilled, return a positive integer, otherwise return -1.**

_Note:_

The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

**Example:**

`h = 3, bounce = 0.66, window = 1.5, result is 3`

`h = 3, bounce = 1, window = 1.5, result is -1`

`(Condition 2) not fulfilled).`

----------
- [ ] **Scramblies (5 kyu)**

Complete the function `scramble(str1, str2)` that returns `True` if a portion of `str1` characters can be rearranged to match `str2`, otherwise returns `False`.

**Notes:**

* Only lower case letters will be used (a-z). No punctuation or digits will be included.
* Performance needs to be considered

`Input strings s1 and s2 are null terminated.`


_Examples_

`scramble('rkqodlw', 'world') ==> True`

`scramble('cedewaraaossoqqyt', 'codewars') ==> True`

`scramble('katas', 'steak') ==> False`
