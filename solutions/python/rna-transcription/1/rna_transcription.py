def to_rna(dna_strand):
    rna_counterparts={'G':'C','C':'G','T':'A','A':'U'}
    rna_strand=''
    for protein in dna_strand:
        rna_strand+=rna_counterparts[protein]
    return rna_strand
