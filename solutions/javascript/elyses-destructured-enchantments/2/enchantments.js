/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Get the first card in the given deck
 *
 * @param {Card[]} deck
 *
 * @returns {Card} the first card in the deck
 */
export function getFirstCard(deck) {
  const [card1, ...theRest]=deck;
  return card1;
}

/**
 * Get the second card in the given deck
 *
 * @param {Card[]} deck
 *
 * @returns {Card} the second card in the deck
 */
export function getSecondCard(deck) {
  const [card1,card2, ...theRest]=deck;return card2;
}

/**
 * Switch the position of the first two cards in the given deck
 *
 * @param {Card[]} deck
 *
 * @returns {Card[]} new deck with reordered cards
 */
export function swapTopTwoCards(deck) {
  let [card1, card2, ...theRest] = deck;
  return [card2, card1, ...theRest];
}


export function discardTopCard(deck) {
  const [card1,...theRest]=deck;
  return [card1,theRest];
}

/** @type {Card[]} **/
const FACE_CARDS = ['jack', 'queen', 'king'];

/**
 * Insert face cards into the given deck
 *
 * @param {Card[]} deck
 *
 * @returns {Card[]} new deck where the second,
 * third, and fourth cards are the face cards
 */
export function insertFaceCards(deck) {
  const [card1,...otherCards]=deck;
  const face_cards=['jack', 'queen', 'king'];
  return [card1,...face_cards,...otherCards];
}
