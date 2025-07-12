/// <reference path="./global.d.ts" />
//
// @ts-check

/**
 * Determine the price of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
const prices={
    Margherita: 7,
    Caprese: 9,
    Formaggio: 10,
    ExtraToppings:2,
    ExtraSauce:1,
}
export function pizzaPrice(pizza, ...extras) {
  if (extras.length<1){
    return prices[pizza]
  }
  let extra=extras.shift()
  return pizzaPrice(pizza, ...extras)+prices[extra]
}

export function orderPrice(pizzaOrders) {
  let priceArray=pizzaOrders.map(order => pizzaPrice(order.pizza, ...order.extras));
  let total=0
  for (const price of priceArray){
    total+=price
  }
  return total
}
