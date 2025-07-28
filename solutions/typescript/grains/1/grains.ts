export const square = (square: number): bigint => {
  if (square < 1 || square > 64){
    throw new Error('square must be between 1 and 64')
  }
  return 2n ** (BigInt(square) - 1n);
};

export const total = (): bigint => {
  return 2n**64n - 1n;
};
