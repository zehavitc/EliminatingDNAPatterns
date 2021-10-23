# Eliminating unwanted patterns with minimal interferences

This directory includes an implementation of an efficient app to eliminate unwated patterns from a DNA sequence.  

## Description

The algorithms implemented here are based of the work described here: https://arxiv.org/abs/2108.05848 (see Algorithm 4) 

## Getting Started

To eliminate unwanted patterns from a DNA you should run eliminate_patterns_from_dna_app.py with the following input parameters:

* Sequence file (-s \ --sequence_file) - contains a raw DNA sequence: lower-case letters indicate
positions that are allowed to be changed, and upper-case letters indicate
positions that are not allowed to be changed. We use IUPAC standard
letters to indicate ambiguity in base specification. 
* Patterns file (-p \ --patterns_file) -  contains a comma-separated list of patterns to elimi-
nate. We use IUP AC standard letters to indicate ambiguity in base specification.
* Optional result file (-r \ --result_file) - the path to which the result should be written, if
not specified, the result will be printed to the console.
 * Optional cost unit (-c \ --cost_unit)- the cost of substituting a letter. The default is 1.
 * Optional transition transversion ratio (-t \ --transition_transversion_proportion) - the cost of a letter substitution that results in a transversion (i.e., {A, G} ↔ {C, T})
 is defined as cost unit × transition transversion ratio. The default ratio is 1.
 
 Example: 
 python .\eliminate_patterns_from_dna_app.py -p c:\patterns.txt -s sequence.txt -r results.txt -c 2 -t 1.5

### Dependencies

This project was implemented using Anaconda (Python 3.7.1). 

## Authors

Zehavit Leibovich (zehavitc@gmail.com)

## Acknowledgments

This work was part of my thesis and was carried out under the supervision of Dr. Ilan Gronau, the Efi Arazi School of Computer Science, The Interdiciplinary Center, Herzliya.
