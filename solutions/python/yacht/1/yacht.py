#Four-of-a-kind function
def four_of_kind(dice):
    occurences=[0,0,0,0,0,0]
    for die in dice:
        occurences[die-1]+=1
    for die,roll_num in enumerate(occurences):
        if roll_num>=4:
            return (die+1)*4
    return 0
#Score categories as lambdas.
YACHT = lambda dice: 50 if len(set(dice))==1 else 0
ONES = lambda dice: dice.count(1)
TWOS = lambda dice: dice.count(2)*2
THREES = lambda dice: dice.count(3)*3
FOURS = lambda dice: dice.count(4)*4
FIVES = lambda dice: dice.count(5)*5
SIXES = lambda dice: dice.count(6)*6
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice))==2 and (dice.count(1)==2 or dice.count(2)==2 or dice.count(3)==2 or dice.count(4)==2 or dice.count(5)==2 or dice.count(6)==2) else 0
FOUR_OF_A_KIND = lambda dice: four_of_kind(dice)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)
# score() is kept simple
def score(dice, category):
    return category(dice)
