from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, TreeConstructor, MultipleSeqAlignment, \
	DistanceCalculator
from Bio.Phylo import draw
from Bio import SeqIO, AlignIO, Seq
import os


def label_func(x):
	return None


def padd_sequnces(input_file):
	global record
	records = SeqIO.parse(input_file, 'fasta')
	records = list(records)  # make a copy, otherwise our generator
	# is exhausted after calculating maxlen
	maxlen = max(len(record.seq) for record in records)
	# pad sequences so that they all have the same length
	for record in records:
		if len(record.seq) != maxlen:
			sequence = str(record.seq).ljust(maxlen, '.')
			record.seq = Seq.Seq(sequence)
	assert all(len(record.seq) == maxlen for record in records)
	# write to temporary file and do alignment
	output_file = '{}_padded.fasta'.format(os.path.splitext(input_file)[0])
	with open(output_file, 'w') as f:
		SeqIO.write(records, f, 'fasta')


def find_duplicates(file):
	with open(file, "r") as f:
		lines = f.readlines()
		names = []
		for line in lines:
			if line.startswith(">"):
				names.append(line)

	names_set = set(names)
	for name in names_set:
		if names.count(name) > 1:
			print(name)


if __name__ == "__main__":
	data = "world_padded.fasta"
	alignment = AlignIO.read(data, "fasta")
	tree_constructor = DistanceTreeConstructor(distance_calculator=DistanceCalculator('identity'))
	tree = tree_constructor.build_tree(alignment)
	draw(tree=tree, label_func=label_func)
