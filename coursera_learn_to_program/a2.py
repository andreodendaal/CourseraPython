def main():
    print(get_complementary_sequence('AT'))

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return sum([1 for elem in dna if elem == nucleotide])


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G'.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGD')
    False
    >>> is_valid_sequence('ZTCGG')
    False

    """
    valid_sequence = 'ATCG'

    for elem in dna:
        if elem not in valid_sequence:
            return False

    return True


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2 )
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 1 )
    'CATCGG'
    >>> insert_sequence('CCGG', 'AT', 0 )
    'ATCCGG'
    >>> insert_sequence('CCGG', 'AT', -1 )
    'CCGATG'

    """
    target_sequence = dna1[:index] + dna2 + dna1[index:]

    return target_sequence

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    >>> get_complement('Z')
    ''

    """
    source = 'ACGT'
    complement = 'TGCA'

    if nucleotide in source:

        idx = source.index(nucleotide)
        match = complement[idx: idx + 1]
        return match

    else:

        return ''


def get_complementary_sequence(dna_sequence):
    """ (str) -> str

        Return the DNA sequence that is complementary to the given DNA sequence

        >>> get_complementary_sequence('AT')
        'TA'
        >>> get_complementary_sequence('CG')
        'GC'
        >>> get_complementary_sequence('AC')
        'CA'
        >>> get_complementary_sequence('CT')
        'TC'
        """

    first_bit = dna_sequence[0:1]
    second_bit = dna_sequence[1:]

    return second_bit + first_bit





if __name__ == 'main':
    main()
