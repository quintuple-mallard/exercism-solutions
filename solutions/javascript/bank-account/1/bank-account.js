//
// This is only a SKELETON file for the 'Bank Account' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class BankAccount {
  #open;
  #balance;
  constructor() {
    this.#open = false;
    this.#balance = 0;
  }

  open() {
    if (this.#open) throw new ValueError("Already open");
    this.#balance = 0;
    this.#open = true;
  }

  close() {
    if (!this.#open) throw new ValueError("Not open");
    this.#open = false;
  }
  #deposit(balance) {
    this.#balance += balance;
  }
  deposit(balance) {
    if (!this.#open) throw new ValueError("Not open");
    if (balance < 0) throw new ValueError("Cannot deposit negative amount");
    this.#deposit(balance);
  }

  withdraw(balance) {
    if (!this.#open) throw new ValueError("Not open");
    if (balance < 0) throw new ValueError("Cannot withdraw negative amount");
    if (balance > this.#balance) 
      throw new ValueError("Cannot withdraw more than current balance");
    this.#deposit(-balance);
  }

  get balance() {
    if (!this.#open) throw new ValueError("Not open");
    return this.#balance;
  }
}

export class ValueError extends Error {
  constructor() {
    super('Bank account error');
  }
}
