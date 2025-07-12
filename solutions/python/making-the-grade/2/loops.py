"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded=[]
    for score in student_scores:
        rounded.append(round(score))
    return rounded

def count_failed_students(student_scores):
    fails=0
    for score in student_scores:
        if not score>40:
            fails+=1
    return fails
def above_threshold(student_scores, threshold):
    the_best=[]
    for score in student_scores:
        if score>=threshold:
            the_best.append(score)
    return the_best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    theresholds=[]
    interval=(highest-40)/4
    for n in range(1,5):
        theresholds.append(int(41-interval+interval*n))
    return theresholds
    


def student_ranking(student_scores, student_names):
    counter=0
    rankings=[]
    for item in student_scores:
        counter+=1
        rankings.append(str(counter)+'. '+student_names[counter-1]+': '+str(item))
    return rankings

def perfect_score(student_info):
    for student in student_info:
        if student[1]==100:
            return student
    return []