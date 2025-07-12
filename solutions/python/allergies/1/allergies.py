def to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return 0 or binary
ALLERGIES=['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate','pollen','cats' ]
class Allergies:
    def __init__(self, allergy_score):
        allergies=[]
        for i,digit in enumerate(reversed(to_binary(allergy_score))):
            if int(digit) and i<8:
                allergies.append(ALLERGIES[i])
        self.allergies=allergies

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies
