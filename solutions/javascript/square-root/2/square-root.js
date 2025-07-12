export const squareRoot = (num) => {
  let root=0
  for (;root*root!==num;root++){}
  return root
};
