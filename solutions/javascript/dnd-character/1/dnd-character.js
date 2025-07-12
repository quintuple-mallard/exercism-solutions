//
// This is only a SKELETON file for the 'D&D Character' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const abilityModifier = (con) => {
  if (con<3){
    throw new Error("Ability scores must be at least 3")
  }
  if (con>18){
    throw new Error("Ability scores can be at most 18")
  }
  return Math.floor((con - 10) / 2);
};

export class Character {
  constructor(){
    this.str = Character.rollAbility();
    this.dex = Character.rollAbility();
    this.con = Character.rollAbility();
    this.int = Character.rollAbility();
    this.wis = Character.rollAbility();
    this.cha = Character.rollAbility();
  }
  static rollAbility() {
    const rolls =  [Math.floor(1 + (Math.random() * 6)),Math.floor(1 + (Math.random() * 6)),Math.floor(1 + (Math.random() * 6)),Math.floor(1 + (Math.random() * 6))];
    const topRolls = rolls.sort().slice(-3,)
    return topRolls.reduce((partialSum, a) => partialSum + a, 0);
  }
  get strength() {
    return this.str;
  }

  get dexterity() {
    return this.dex;
  }

  get constitution() {
    return this.con;
  }

  get intelligence() {
    return this.int;
  }

  get wisdom() {
    return this.wis;
  }

  get charisma() {
    return this.cha;
  }

  get hitpoints() {
    return 10 + abilityModifier(this.con);
  }
}
