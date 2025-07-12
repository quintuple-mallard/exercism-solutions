/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */
export function cookingStatus(remainingTime){
  switch (remainingTime){
    case 0:
      return 'Lasagna is done.'
      break;
    case undefined:
      return 'You forgot to set the timer.'
      break;
    default :
      return 'Not done, please wait.'
      break;
  }
}
export function preparationTime(layers, timePerLayer) {
  if (timePerLayer===undefined){
    return layers.length*2;
  }
  return layers.length*timePerLayer;
}
export function quantities(layers) {
  let noodlesAndSauce={'noodles':0,'sauce':0}
  for (let layer of layers){
    if (layer=='sauce'){
      noodlesAndSauce['sauce']+=0.2;
    }
    else if (layer=='noodles'){
      noodlesAndSauce['noodles']+=50;
    }
  }
  return noodlesAndSauce;
}
export function addSecretIngredient(friendRecipe,myRecipe) {
  myRecipe.push(friendRecipe[(friendRecipe.length-1)]);
}
export function scaleRecipe(recipeForTwo, portions) {
  let recipe={}
  for (let ingredient in recipeForTwo){
    recipe[ingredient]=recipeForTwo[ingredient]*(portions/2);
  }
  return recipe;
}