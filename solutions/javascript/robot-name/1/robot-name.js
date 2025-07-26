export class Robot {
  static releaseNames = () => Robot.usedNames = new Set()
  static usedNames = new Set()
  static generateName = () => {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const randomLetter = () => alphabet[Math.floor(Math.random() * 26)]
    return `${randomLetter()}${randomLetter()}${Math.floor(Math.random() * 9)}${Math.floor(Math.random() * 9)}${Math.floor(Math.random() * 9)}`
  };
  get name() {
    return this._name
  }
  constructor() {
    let name = Robot.generateName();
    while (Robot.usedNames.has(name)){
      name = Robot.generateName();
    }
    this._name = name;
    Robot.usedNames.add(name)
  }
  reset() {
    let name = Robot.generateName();
    while (true){
      if (Robot.usedNames.has(name)){
        name = Robot.generateName();
      } else {
        break;
      }
    }
    this._name = name;
    Robot.usedNames.add(name);
  }
}