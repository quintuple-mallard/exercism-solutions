//
// This is only a SKELETON file for the 'Error handling' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const processString = (input) => {
  try {
    if (typeof input !== "string") {
      throw new TypeError("Input must be a string");
    } else if (input === "") {
      return null;
    } else if (input.length < 10 || input.length > 100) {
      throw new RangeError("Invalid string length (must be >=10 and <=100)");
    } else if (/\d/.test(input)) {
      throw new SyntaxError("String must be alphabetic");
    } else return input.toUpperCase()
  } catch (e) {
    console.log(e.message);
    throw e;
  }
};
