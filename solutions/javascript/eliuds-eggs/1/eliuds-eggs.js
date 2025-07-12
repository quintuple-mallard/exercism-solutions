//Just my Python solution
function toBinary(number){
  let binary = ''
  while (number > 0){
    binary = String(number % 2) + binary
    number = Math.floor(number / 2)
  }
  return binary;
}
export function eggCount(displayValue){
  let count=0
  for (const digit of toBinary(displayValue)){
    if (digit==='1'){count++}
  }
  return count
}