const rnaCounterparts={G:'C',C:'G',T:'A',A:'U'}
export const toRna = (dna) => {
  return dna.split('').map(nucleotide=>rnaCounterparts[nucleotide]).join('');
};
