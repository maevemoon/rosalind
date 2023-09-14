# 6 HAMM Counting Point Mutations

# from the Hidden Messages project
def HammingDistance(s, t):
    count = 0
    for i in range(len(s)):
        # we have to assume that the lengths of the two strings are the same
        # then we check each of their positions and see if its symbol is equal to the other strings
        if len(s) == len(t) and s[i] != t[i]:
            count = count+1
    return count

s = "GACGGAGCGGTACCTCAGCTACGCGAATAATCGGTATCGAGTCTCACTGGCGCCTTACGCGATTGTCAGTATACTATGCTCTGTGTTCTAAACTAATGTAGTCTTGCTTTGCCGAGACGGGGCCCGGTATGAAAGGGCACAGGTTGGAGAGTAAGGGCGGTTGTTTTGCAGTCATCAATCACGGAGACCCAATTACAGGTTCGTCACTGGCGGTACCACTTGGCCGTGGCGTCCCACTCGAATCGTGGGCATACCTTCAACGTAAAATTGGTCTCCTACTCCCGCACCAGTCACTCGGCTATTTTCGGAGGGCAGCATACGGACGAAAGTTCCAGTAACTAGGGCGAAAGCAATGTTTGTATGATCAAGTATATACGCTCCTTAGGGTTGATGACTTACGCTTCATAACGTACCGGAAGTGCATAGCCCTCACCCCATTAACTGTATTCAGGCTACAAAGGCCCGAGCGCTCTTCTCGTGGAAATGGGAGAGTGCTGAAGAGCTCTCAAGGAGACTGTGCCGGGCATATGATCATCCCTCATACCGCACATCGATCAGAATCGGAATTCCCAAATCCACCGCACCGAGAGAGATTTGTCGTGATACGAGCGTCCCCTTGCCTATGGTCCCTTCTCCTTCACCTAATTGGGCTACATTCAAAGACGCAGAAGAAGCGTCGTTAACGTTAGGGACTCCGAACACTCTAGACGCAGTAGATGCGTCCTTGGAACTCAACCTCGCTGTTCGCAAAAAGGGCCGGAGTAGGATGACTCCATAACACTCAGGGGACATTTACCCCCTTGTAAAGACTCTTGAAGCTATTTCTACCGTTGGTGGCGAAGTGCGCAGTATGCGCGCCCGTACCGACTCACACTGCCAATAAGCGTCTCACCGGTCTCGCACAACTACTTTTAATCGGAGACACCACTGTTAGGCCCCATA"
t = "CTGCGGGTTTTAGATCCGCTACTCTAAAGGACGGTATAGATACTTCCGGGCGCGTAAACTGTGGGGAAATGAAGTTAGAACACTGTGCGAAGTCAATGAGCTCGTGCTTCAATTAGATGCTATTTAGGAAGAAATTTCCTCCGTCGCCACGGTAACGATTGCGCAGTGCATGCATGACCTACCCAGCCGGGATCGTGGGTTCGACACTGCTTTGACAGCATCGTCACGACGTCACCCTCCCGTCCTGATGTGTAAATAGTCGGGATAATCGAGTCATGATCTCGCATCATTAGACCGTATGTTCTCGGAGTCCCAACCACCACCAACAGATCCTGTCAATATCGAGGACGTTATGTACGAGCCCTGGCCCAGGCAACTTCCATCGGTTGGATCGGAATTGCAGCCAGACTTATCTTATGCTCGCATCCCACTCTGCTACGCCTCTATAGATACTCGATCGGGTAGATAGCATGTATCTTCCACGTAACAGACGCGGGTACAGGAATCAAGTAAGCAGTGCCTTGCCTACGATAAGGTCTCCCACTGTAATAGGACCACATAATCAAGCGCCAACTCAATCTAGCCTAAAGTAATGATATGAGAACCGTGCATAGCGCTCACCAAGATCAATTCGTCATTATTCGCAGTAGATACGTTCACAGACACATGAATACGATCGTTCATTGTTACCTCCGCCAACGTTCTTGGTGCATGAGGTGTGTCCATGGAACTCCTGCGCAATTCATTGGAAAAGGGCCGCGGAAAGCCGACACCCGACCAGTCCCCGTGAGTCTCGCTCGTTGTACGGACATGGCAAGCTGTAGCAACCGTTTGTGGTCGCACAAGCTGTCTTAGAACCCACCCCTGACTTACCTGACATTGAGGGCCTCGGGGCGTTAGCTGTTCCGCCCTTATGCCGGCACGCGACTGCTATTACCCCGC"


print(HammingDistance(s, t))