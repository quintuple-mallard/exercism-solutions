export class Squares {
  constructor(num) {
    this.num = num;

  }

  get sumOfSquares() {
    return this.#range(this.num)
      .map(item => item ** 2)
      .reduce(
        (acc, item) => acc + item,
        0
      )
  }

  get squareOfSum() {
    return this.#range(this.num).reduce(
      (acc, item) => acc + item, 0
    ) ** 2
  }

  get difference() {
    return this.squareOfSum - this.sumOfSquares
  }
  #range(n) {
    const rangeArray = [];
    for (let i = 0; i < n + 1; i++) rangeArray.push(i)
    return rangeArray
  }
}
