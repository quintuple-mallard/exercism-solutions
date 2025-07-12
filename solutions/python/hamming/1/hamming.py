def distance(strand_a, strand_b):
    hamming_distance=0
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for idx,char in enumerate(strand_a):
        if char!=strand_b[idx]:
            hamming_distance+=1
    return hamming_distance