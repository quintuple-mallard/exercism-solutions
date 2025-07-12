# Globals for the directions
# Change the values as you see fit
EAST = 90
NORTH = 0
WEST = 270
SOUTH = 180


class Robot:
    """Class for simulating a robot moving on a grid."""
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._x = x_pos
        self._y = y_pos
        self._direction = direction

    @property
    def coordinates(self):
        return (self._x, self._y)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_direction):
        self._direction = new_direction
    def move(self,instructions):
        for char in instructions:
            if char == 'R':
                self._direction += 90
                self._direction %= 360
            elif char == 'L':
                self._direction -= 90
                self._direction %= 360
            else:
                if self._direction == 0:
                    self._y+=1
                elif self._direction == 90:
                    self._x+=1
                elif self._direction == 180:
                    self._y-=1
                else:
                    self._x-=1

