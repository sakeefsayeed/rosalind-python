from Bio import Entrez

Entrez.email = "sakeefsayeed@gmail.com"
handle = Entrez.esearch("nucleotide",
                        # Genus name                    # Start Publication Date         # End Publication Date
                        '"Sinobambusa"[Organism] AND ''"2005/04/17"[Publication Date] : "2010/11/29"[Publication Date]')
record = Entrez.read(handle)
print(record["Count"])
