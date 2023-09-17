# 9 SUBS Finding a Motif in DNA

# from the Hidden Messages project
def PatternMatching(t,s):
    positions = []
    a = len(s)
    b = len(t)
    for i in range(a-b+2):
        if s[i:i+b] == t:
            # adding +1 to the position to follow Rosalind's definition
            positions.append(i+1)
    return positions

t = "CTTCGCTCT"
s = "CTTCGCTCTTCGCTCTAACTTCGCTCTGGGCACCCTTCGCTAAATCTTCGCTTACTTCGCTCTTCGCTACTTCGCTTTGTCTTCGCTCCTGGGGACCCTTCGCTCTTCGCTGGTTAAATCTTCGCTGATCCGCGCTTCGCTGGTCAAAGGGTCTTCGCTGGATAACTGTCATGCGCCGCTTCGCTCTTCGCTCTTCGCTCTTCGCTTGCTTCGCTCTTCGCTGCGGGCTCAGAAGCTTCGCTTCTTCGCTAGCTTCGCTGTCTTCGCTATACTTCGCTCTTCGCTCTTCGCTCACACGCTTCGCTCTTCGCTTACCCTTCGCTCTTCGCTTCTTCGCTTTATAACTTCGCTTCGCTCGCCCTTCGCTATCAAAGAACGGCCTTCGCTGTCGCTTCGCTCTTCGCTCTTCGCTCTTCGCTAACTTCGCTCTTCGCTTTCGGGTCTTCGCTCTTGCAGCTTCGCTGCAGTCTTCGCTCTTCGCTTCATCTTCGCTCTTCGCTCCTTCGCTAGAGGCTTCGCTCCTTCGCTGCTTCGCTCTTCGCTTGGCTTCGCTCGTACCGCTTCGCTCCCTTCGCTCTTCGCTCCCTCTTCGCTTCGGCTTCGCTGCATCTTCGCTCCTTCGCTCTTCGCTTGGCTTCGCTTTCTTCGCTCGCTTCGCTAGCTTCGCTATCATACCTTCGCTACTTCGCTCTTCGCTAGTATCTTCGCTCTTCGCTCTTCGCTCCTTCGCTTTTCTTCGCTCTTCGCTCTTCGCTGTACTTCGCTACAAACTTCGCTGGCTTCGCTTGACAGTTATATCTTCGCTACTTCGCTGTAGCCTTCGCTAGCTTCGCTCTTCGCTCTTCGCTCCACTTCGCTGCTTCGCTACTTCGCTCATTCTTCGCTGAGCCTTCGCT"
print(PatternMatching(t,s))