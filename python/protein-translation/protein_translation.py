def proteins(strand):

    codons = [strand[i:i+3] for i in range(0, len(strand),3)]

    protein_dict = {
        'AUG':'Methionine',
        'UUU':'Phenylalanine',
        'UUC':'Phenylalanine',
        'UUA':'Leucine',
        'UUG':'Leucine',
        'UCU':'Serine',
        'UCC':'Serine',
        'UCA':'Serine',
        'UCG':'Serine',
        'UAU':'Tyrosine',
        'UAC':'Tyrosine',
        'UGU':'Cysteine',
        'UGC':'Cysteine',
        'UGG':'Tryptophan',
        'UAA':'STOP',
        'UAG':'STOP',
        'UGA':'STOP'
    }

    polypeptide = [protein_dict[codon] for codon in codons]
    if 'STOP' in polypeptide:
        return polypeptide[:polypeptide.index('STOP')]
    else:
        return polypeptide