
from itertools import product
from constants import dna_iupac_dict

def extend_ambiguous_dna(seq):

    """
    :param seq: a DNA sequence, possibly with IUPAC code (upper cased)
    :return: return list of all possible sequences given an ambiguous DNA input seq,
    based on https://www.bioinformatics.org/sms/iupac.html
    gap (. or - ) are not supported
    """
    #TODO - check that the sequence is valid (only DNA letters)
    return list(map("".join, product(*map(dna_iupac_dict.get, seq))))

def is_purine(letter):
    lower_letter = letter.lower()
    return lower_letter == "a" or lower_letter == "g"

def is_pyrimidine(letter):
    lower_letter = letter.lower()
    return lower_letter == "c" or lower_letter == "t"

def is_transition(old, new):
    return (is_purine(old) and is_purine(new)) or (is_pyrimidine(old) and is_pyrimidine(new))

def is_transversion(old,new):
    return not(is_transition(old,new))

def contains_transversion(list):
    found_pyrimidine = False
    found_purine = False
    for letter in list:
        if is_pyrimidine(letter):
            found_pyrimidine = True
        else:
            found_purine = True
    return found_purine and found_pyrimidine
