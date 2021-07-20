from Bio import SeqIO
from Bio.SeqUtils import GC
name = ''
max = 0
for seq_record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    x = GC(seq_record.seq)
    if x > max:
        max = x
        name = seq_record.id

print(name)
print(max)
