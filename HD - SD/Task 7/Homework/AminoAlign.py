# ================================ Part 3 of Compulsory Task ===========================
# Create a new program called AminoAlign.py with a function named align
# This function must take in any two amino acid sequences and find all characters in which they differ.
# Run this function on the output of Part 2 (The AA of the mutatedDNA.txt file vs the AA of the normalDNA.txt file)
# and identify the mutated amino acid. You can compare strings like this print("a" == "b")


def align():
    seq1 = open("normal_dna.txt").read()
    seq2 = open("mutated_dna.txt").read()
    while len(seq1) and len(seq2) != 0:
        for x in seq1:
            for y in seq2:
                if x == y:
                    continue
                elif x != y:
                    print("Irregularities: {}  and {}". format(x, y))
                    continue
                else:
                    break


print(align())
