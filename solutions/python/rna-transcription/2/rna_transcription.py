def to_rna(dna_strand):
    rna_counterparts={'G':'C','C':'G','T':'A','A':'U'}
    return ''.join([rna_counterparts[letter] for letter in dna_strand])
