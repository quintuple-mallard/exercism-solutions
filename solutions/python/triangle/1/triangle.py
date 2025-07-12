def equilateral(sides):
    for side in sides:
        if not side:
            return False
    if sides[0]==sides[1] and sides[1]==sides[2]:
        return True
    return False
def isosceles(sides):
    for side in sides:
        if not side:
            return False
    if sides[0]+sides[1]<=sides[2] or sides[0]+sides[2]<=sides[1] or sides[1]+sides[2]<=sides[0]:
        return False
    if (sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]):
       return True
    return False

def scalene(sides):
    if sides[0]+sides[1]<=sides[2] or sides[0]+sides[2]<=sides[1] or sides[1]+sides[2]<=sides[0]:
        return False
    if sides[0]!= sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    return False
