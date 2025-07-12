"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created=0
    def __init__(self,x,y):
        self.x_coordinate=x
        self.y_coordinate=y
        self.health=3
        Alien.total_aliens_created+=1
    def hit(self):
        self.health-=1
    def is_alive(self):
        return self.health>0
    def teleport(self,new_x,new_y):
        self.x_coordinate=new_x
        self.y_coordinate=new_y
    def collision_detection(self,other_object):
        pass
    

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(positions):
    aliens = []
    for position in positions:
        aliens.append(Alien(position[0],position[1]))
    return aliens