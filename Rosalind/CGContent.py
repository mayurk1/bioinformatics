from Bio import SeqIO
from Bio.SeqUtils import GC

name = ''
max = 0
for seq_record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    if GC(seq_record.seq) > max:
        max = GC(seq_record.seq)
        name = seq_record.id

print(name)
print(max)
