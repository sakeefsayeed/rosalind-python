from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('Q5SLP9')
record = SwissProt.read(handle)

for x in range(len(record.cross_references)):
    ID = record.cross_references[x][0]
    if ID == 'GO':
        firstChar = record.cross_references[x][2][0]
        if firstChar == 'P':
            bioProcess = record.cross_references[x][2]
            print(bioProcess[2:])