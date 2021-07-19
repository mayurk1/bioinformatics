from Bio import SeqIO

#records = list(SeqIO.parse('rosalind_gc.txt', "fasta"))

records = ""

gc = 0


for x in records:
    if x == 'G' or 'C':
        gc += 1

print(gc)