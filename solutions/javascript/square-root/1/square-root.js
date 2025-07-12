//
// This is only a SKELETON file for the 'Square root' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const squareRoot = (num) => {
  let root=0
  while (root*root!==num){
    root+=1
  }
  return root
};
