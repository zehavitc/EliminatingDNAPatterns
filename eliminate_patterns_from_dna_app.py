import getopt
import sys
from patterns_reader import PatternsReader
from sequence_reader import SequenceReader
from dna_utils import extend_ambiguous_dna
from multiple_soft_elimination import MultipleSoftElimination
from cost import Cost
from constants import dna_alphabet

help_str = "-p <patterns_file> -s <sequence_file> [-r <result_file>]"

def eliminate(patterns, sequence, cost_unit, transition_transversion_proportion):
    extended_patterns = extend_embiguous_patterns(patterns)
    cost = Cost(sequence, cost_unit, transition_transversion_proportion)
    result_seq = MultipleSoftElimination(sequence=sequence, patterns=extended_patterns, cost=cost, alphabet=dna_alphabet).eliminate()
    result_cost = cost.get_cost_of_seq(result_seq)
    return result_seq, result_cost

def app(argv):
    patterns_file_path,sequence_file_path, result_file_path, cost_unit, transition_transversion_proportion = handle_input_params(argv)
    patterns = PatternsReader().read_from_file(patterns_file_path)
    sequence = SequenceReader().read_from_file(sequence_file_path)
    result_seq, result_cost = eliminate(patterns=patterns, sequence=sequence, cost_unit=cost_unit, transition_transversion_proportion=transition_transversion_proportion)
    if result_file_path is None:
        print("result sequence: " + result_seq)
        print("cost: " + str(result_cost))
    else:
        with open(result_file_path, "w") as result_file:
            result_file.write(result_seq)
    return result_seq, result_cost




def extend_embiguous_patterns(patterns_file_path):
    extended_patterns_list = [extend_ambiguous_dna(p) for p in patterns_file_path]
    extended_patterns_flat = []
    for extended_patterns in extended_patterns_list:
        extended_patterns_flat.extend(extended_patterns)
    return extended_patterns_flat


def handle_input_params(argv):
    patterns_file_path = None
    sequence_file_path = None
    result_file_path = None
    cost_unit = None
    transition_transversion_proportion = None
    try:
        opts, args = getopt.getopt(argv, "hp:s:r:c:t", ["patterns_file=", "sequence_file=", "result_file=", "cost_unit=", "transition_transversion_proportion="])
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
        elif opt in ("-r", "--result_file"):
            result_file_path = arg
        elif opt in ("-c", "--cost_unit"):
            cost_unit = arg
        elif opt in ("-t", "--transition_transversion_proportion"):
            transition_transversion_proportion = arg
    if patterns_file_path is None or sequence_file_path is None:
        print(help_str)
        sys.exit()
    return patterns_file_path, sequence_file_path, result_file_path, cost_unit, transition_transversion_proportion


if __name__ == "__main__":
   app(sys.argv[1:])