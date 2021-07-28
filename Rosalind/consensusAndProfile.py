""""
Consensus and Profile
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus
strings exist, then you may return any one of them.)
"""
from Bio import SeqIO

records = []
for seq_record in SeqIO.parse("rosalind_cons.txt", "fasta"):
    records.append(str(seq_record.seq))

# Make DNA profile
aProfile = []
cProfile = []
gProfile = []
tProfile = []

aTally = 0
cTally = 0
gTally = 0
tTally = 0

n = 0
m = 0
while n < len(records[0]):
    for seq in records:
        if seq[n] == 'A':
            aTally += 1
        if seq[n] == 'C':
            cTally += 1
        if seq[n] == 'G':
            gTally += 1
        if seq[n] == 'T':
            tTally += 1

    aProfile.append(aTally)
    cProfile.append(cTally)
    gProfile.append(gTally)
    tProfile.append(tTally)

    aTally = 0
    cTally = 0
    gTally = 0
    tTally = 0

    n += 1

# Generate consensus string
consensus = ''
m = 0
while m < len(aProfile):
    high = 0
   # current = ''
    if aProfile[m] > high:
        current = 'A'
        high = aProfile[m]
    if cProfile[m] > high:
        current = 'C'    
        high = cProfile[m] 
    if gProfile[m] > high:
        current = 'G'
        high = gProfile[m]
    if tProfile[m] > high:
        current = 'T'
        high = tProfile[m]
    consensus += current
    m += 1

print(consensus)
print("A: ", *aProfile, sep=' ')
print("C: ", *cProfile, sep=' ')
print("G: ", *gProfile, sep=' ')
print("T: ", *tProfile, sep=' ')
