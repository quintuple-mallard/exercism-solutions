protein_translation = {
    'AUG' :'Methionine',
'UUU' :'Phenylalanine', 'UUC' :'Phenylalanine',
'UUA':'Leucine', 'UUG' :'Leucine',
'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG' :'Serine',
'UAU':'Tyrosine', 'UAC' :'Tyrosine',
'UGU':'Cysteine', 'UGC' :'Cysteine',
'UGG' :'Tryptophan',
}
def get_codons(strand):
    codons = []
    for i in range(0,len(strand),3):
        codons.append(strand[i:i+3])
    return codons
def proteins(strand):
    translated = []
    for codon in get_codons(strand):
        if codon in ['UAA', 'UAG', 'UGA']:
             break
        translated.append(protein_translation[codon])
    return translated
