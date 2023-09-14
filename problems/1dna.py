# 1 DNA Counting DNA Nucleotides

def NucelotideCount(Text):
    counta = 0
    countc = 0
    countg = 0
    countt = 0
    for i in range(len(Text)):
        if Text[i] == "A":
            counta+=1
        elif Text[i] == "C":
            countc+=1
        elif Text[i] == "G":
            countg+=1
        elif Text[i] == "T":
            countt+=1
    nucelotidecount = "{} {} {} {}".format(counta, countc, countg, countt)
    return nucelotidecount

Text = "TTAAATTGTGTGGCTCCATGTGACCCTCTGTCGTAGTGATGGGGGCAGTCTCCAATATAACCATGAGGCCTAGGAGTGAAAACTCCACCGAGCAGAATGTGGTGAAAATTTCGTTTCGTCGCTCCGGACTTCTAAGTCTGCGGGCGTTCTTTCGCTGTAGCTGCCCTAGTGCAGCGAGGTCTCGCTACTGACTGAAGGCCCAACGAGACCCGCCGTGCTCCCGTAAACTGCTTAAGTCATAGCACGCTCAAAAACAATTTGATGGATTGTTACGCTTGCTTACTAACGCACCCGTGATCTATCGGTTGTTAGCGACATACCAGATTCCTCCAGTCACATCCGCCTCTGGACTGAGACTTAGGTTCTCCACAGTGTTATTTGACGCTTGCCTACTCTGTGCATGCAACATGAGACCTCAAATTTCAATCGGGATGCAGGCTAACTTAGTCGCTTTTTGCAAAGGACATCAACTATAATAATTGTCACCTATGTAGCGATAAATTCATGTACCCGGTGGGTACAATAGTGAGTGGAAATGACTGCGCGTGATGATACTAGTTAAAGCGTTTCTAAATAAACTAGAGCTTCTCAAACATAATGTTCGGAAGAGAATCTAGCACGCACGATAGGCACAGTGGGAGTATCTTAATGCTAGGACACCGCGTCTGGAAGATCAGAAGGTAGCTACTATAGTGAACACCCTTCTTAAAATCCACCAACGTGAAAAGGGCGTTTGCTGGTCCCCCAAGTGGAGTTGCTCCGCCCGAATGTTGCTGACAGATCCCTACTAGCAGCATCGCTCTCCACTCTAGTCAGAAGCCCTCCACATACAATCTTGTTTTTTTGTCCCTTGCCCATTGAG"
print(NucelotideCount(Text))

# SOLUTION

def NucleotideCount(Text):
    return Text.count("A"), Text.count("C"), Text.count("G"), Text.count("T")


