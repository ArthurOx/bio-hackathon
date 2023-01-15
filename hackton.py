import numpy as np
from itertools import groupby
from Bio import AlignIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import MuscleCommandline

def fastaread(fasta_name):
	"""
    Read a fasta file. For each sequence in the file, yield the header and the actual sequence.
    In Ex1 you may assume the fasta files contain only one sequence.
    You may keep this function, edit it, or delete it and implement your own reader.
    """
	f = open(fasta_name)
	faiter = (x[1] for x in groupby(f, lambda line: line.startswith(">")))
	for header in faiter:
		header = next(header)[1:].strip()
		seq = "".join(s.strip() for s in next(faiter))
		yield header, seq

def create_model():
	alignment = list(fastaread('Data/world1.fasta'))
	sequences = []
	for header, sequence in alignment:
	longest_length = max(len(s) for s in alignment)
	padded_sequences = [s.ljust(longest_length, '-') for s in sequences]
	records = (SeqRecord(Seq(s)) for s in padded_sequences)
	SeqIO.write(records, "example.fasta", "fasta")

	j =3

if __name__ == '__main__':
	create_model()