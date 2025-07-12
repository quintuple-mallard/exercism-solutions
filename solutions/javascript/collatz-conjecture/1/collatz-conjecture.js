export function steps(number) {
  if (number<1){throw new Error('Only positive integers are allowed')}
  if(number===1){
    return 0
  }
  for(let i = 0; i < 200; i++) {
    if (number%2===0){
      number/=2
    }
    else{
      number = (number*3)+1
    }
    if(number===1){
      return i+1
    }
  }
}