//
// This is only a SKELETON file for the 'Raindrops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const convert = num => {
  const [pling,plang,plong]=[num%3===0?'Pling':'',num%5===0?'Plang':'',num%7===0?'Plong':'']
  return (pling+plang+plong)||String(num)
}