export const squareRoot = (n, root=1) => {
  if (root * root === n) {
    return root
  }
  return squareRoot(n, root + 1)
}