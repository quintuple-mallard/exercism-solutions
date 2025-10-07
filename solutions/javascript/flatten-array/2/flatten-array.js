export const flatten = array => {
  const newArray = []
  for (let item of array) {
    if (Array.isArray(item)) {
      newArray.push(...item)
    } else {
      newArray.push(item)
    }
  }
  if (newArray.every(item => !Array.isArray(item))) {
    return newArray.filter(item => item !== null && item !== undefined);
  }
  return flatten(newArray);
}
