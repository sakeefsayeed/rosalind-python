from Bio.Seq import Seq

with open("/Users/sakeef/Desktop/Rosalind-Python/resources/rosalind_ini.txt") as fp:
    data = fp.read()
seq = Seq(data)
print(seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T"))
