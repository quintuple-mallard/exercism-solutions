//
// This is only a SKELETON file for the 'Nucleotide Count' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export function countNucleotides(strand) {
  let nucleotides = {A: 0, C: 0, G: 0, T: 0}
  for (const nucleotide of strand) {
    if (!"ACGT".includes(nucleotide)){
      throw new Error('Invalid nucleotide in strand')
    }
    nucleotides[nucleotide]+=1;
  }
  return Object.values(nucleotides).join(' ')
}
