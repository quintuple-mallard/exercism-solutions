//
// This is only a SKELETON file for the 'Flatten Array' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

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
