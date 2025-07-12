def score(word):
    scores=str.maketrans('AEIOULNRSTDGBCMPFHVWYKJXQZ','111111111122333344444588AA')
    score=word.upper().translate(scores)
    score=list(score)
    for index,letter_value in enumerate(score):
        if letter_value=='A':
            score[index]=10
        score[index]=int(score[index])
    return sum(score)