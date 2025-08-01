"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number+1,number+2]
    

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand)/len(hand)
    


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    average=sum(hand)/len(hand)
    upper_and_lower_avg=(hand[0]+hand[-1])/2
    median=hand[int((len(hand)-1)/2)]
    if median==average or upper_and_lower_avg==average:
        return True
    return False
        
    


def average_even_is_average_odd(hand):
    even_nums=[]
    odd_nums=[]
    counter=1
    for num in hand:
        if counter%2==0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
        counter+=1
    if len(even_nums) :
        even_avg=sum(even_nums)/len(even_nums)
    else:
        even_avg=0
    if len(odd_nums):
        odd_avg=sum(odd_nums)/len(odd_nums)
    else:
        odd_avg=0
    if odd_avg==even_avg:
        return True
    return False

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1]==11:
        return hand[:-1]+[22]
    return hand
