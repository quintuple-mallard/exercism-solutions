export function keep(collection, operation){
  let toKeep = [];
  for (const item of collection){
    if (operation(item)){
      toKeep.push(item);
    }
  }
  return toKeep;
}
export function discard(collection, operation){
  let toDiscard = [];
  for (const item of collection){
    if (!operation(item)){
      toDiscard.push(item);
    }
  }
  return toDiscard;
}

