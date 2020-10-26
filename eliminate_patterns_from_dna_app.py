import getopt
import sys
from patterns_reader import PatternsReader
from sequence_reader import SequenceReader
from dna_utils import extend_ambiguous_dna

help_str = "-p <patterns_file> -s <sequence_file>"

def main(argv):
    patterns_file_path,sequence_file_path = handle_input_params(argv)
    patterns = PatternsReader().read_from_file(patterns_file_path)
    sequence = SequenceReader().read_from_file(sequence_file_path)
    extended_patterns = extend_embiguous_patterns(patterns_file_path)



def extend_embiguous_patterns(patterns_file_path):
    extended_patterns_list = [extend_ambiguous_dna(p) for p in patterns_file_path]
    extended_patterns_flat = []
    for extended_patterns in extended_patterns_list:
        extended_patterns_flat.extend(extended_patterns)
    return extended_patterns_flat


def handle_input_params(argv):
    patterns_file_path = None
    sequence_file_path = None
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["patterns_file=", "sequence_file="])
    except getopt.GetoptError:
        print(help_str)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_str)
            sys.exit()
        elif opt in ("-p", "--patterns_file"):
            patterns_file_path = arg
        elif opt in ("-s", "--sequence_file"):
            sequence_file_path = arg
    if patterns_file_path is None or sequence_file_path is None:
        print(help_str)
        sys.exit()
    return patterns_file_path, sequence_file_path


if __name__ == "__main__":
   main(sys.argv[1:])