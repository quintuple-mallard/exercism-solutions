import random as rd
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Robot:
    used_names=[]
    def __init__(self):
        self.name = LETTERS[rd.randint(0, 25)] + LETTERS[rd.randint(0, 25)] + str(rd.randint(0, 9)) + str(rd.randint(0, 9)) + str(rd.randint(0, 9))
        self.used_names.append(self.name)
    def reset(self):
        while True:
            candidate = LETTERS[rd.randint(0, 25)] + LETTERS[rd.randint(0, 25)] + str(rd.randint(0, 9)) + str(rd.randint(0, 9)) + str(rd.randint(0, 9))
            if candidate not in self.used_names:
                self.name=candidate
                break 
            
            
        
