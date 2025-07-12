// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Return each wagon's id in form of an array.
 *
 * @param {number[]} ids
 * @returns {number[]} wagon ids
 */
export function getListOfWagons(...wagons) {
  return wagons;
}

/**
 * Reorder the array of wagons by moving the first 2 wagons to the end of the array.
 *
 * @param {number[]} ids
 * @returns {number[]} reorderd list of wagons
 */
export function fixListOfWagons(ids) {
  const [wagon1,wagon2, ...wagons]=ids;
  return [...wagons, wagon1, wagon2]
}

/**
 * Fixes the array of wagons by inserting an array of wagons after the first element in eachWagonsID.
 *
 * @param {number[]} ids
 * @param {number[]} missingWagons
 * @returns {number[]} corrected list of wagons
 */
export function correctListOfWagons(ids, missingWagons) {
  const [locomotive, ...otherWagons]=ids;
  return [locomotive, ...missingWagons, ...otherWagons]
}

/**
 * Extend route information by adding another object
 *
 * @param {Record<string, string>} information
 * @param {Record<string, string>} additional
 * @returns {Record<string, string>} extended route information
 */
export function extendRouteInformation(information, additional) {
  return {...information,...additional}
}

/**
 * Separate arrival time from the route information object
 *
 * @param {Record<string, string>} information
 * @returns {[string, Record<string, string>]} array with arrival time and object without arrival time
 */
export function separateTimeOfArrival(information) {
  const {timeOfArrival ,...otherInfo}=information;
  return [timeOfArrival, otherInfo]
}
