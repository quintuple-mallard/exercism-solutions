export class InvalidInputError extends Error {
  constructor(message) {
    super();
    this.message = message || 'Invalid Input';
  }
}

export class Robot {
  constructor(){
    this.direction = "north";
    this.pos = [0,0]
  }
  get bearing() {
    return this.direction;
  }
  get coordinates() {
    return this.pos;
  }
  moveRobot() {
    if (this.direction==="north") this.pos[1]+=1
    else if (this.direction==="east") this.pos[0]+=1
    else if (this.direction==="south") this.pos[1]-=1
    else if (this.direction==="west") this.pos[0]-=1
  }
  place({ x, y, direction }) {
    if (!["north","south","east","west"].includes(direction)){
      throw new InvalidInputError()
    }
    this.pos = [x,y];
    this.direction = direction
  }
  static turnLeft = direction => {
    const turns = {north:"west",south:"east",east:"north",west:"south"}
    return turns[direction]
  }
  static turnRight = direction => Robot.turnLeft(Robot.turnLeft(Robot.turnLeft(direction)))
  evaluate(instructions) {
    for (const char of instructions){
      if (char==="R") this.direction = Robot.turnRight(this.direction)
      else if (char==="L") this.direction = Robot.turnLeft(this.direction)
      else this.moveRobot()
    }
  }
}
