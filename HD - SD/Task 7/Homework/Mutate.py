# ================================ Part 2 of Compulsory Task ===========================
# Add another function to the program SickleCellDisease.py called 'mutate'.
# This function must read in the contents of the text file named 'dna.txt'
# It must then identify the first occurrence of the lowercase letter 'a' in 'dna.txt'.
# You must then write two new text files, one named normal_dna.txt and the other named mutated_dna.txt.
# The normal_dna.txt must have the same dna sequence as dna.txt with the 'a' changed to an 'A'.
# The mutated_dna.txt must have the same dna sequence as dna.txt with the 'a' changed to a 'T'.
# Now create a new function, txtTranslate, that calls the translate function that you wrote in Part 1, to take in
# the text file input.
# Call it on both mutated_dna.txt and normal_dna.txt, and output both Amino Acid sequences to the user.


def mutate_normal():
    sqe = open("DNA.txt")
    normal_dna = open("normal_dna.txt", "w+")
    normal_dna.write(sqe.read().replace("a", "A"))
    print(str(translate(open("normal_dna.txt").read())))
    sqe.close()
    normal_dna.close()


def mutate_mutated():
    sqe = open("DNA.txt")
    mutated_dna = open("mutated_dna.txt", "w+")
    mutated_dna.write(sqe.read().replace("a", "T"))
    print(str(translate(open("mutated_dna.txt").read())))
    sqe.close()
    mutated_dna.close()


def translate(dna):
    slc = []
    while len(dna) != 0:
        if len(dna) >= 3:
            codon = dna[0:3]
            if codon == ["A", "T", "T"] or ["A", "T", "C"] or ["A", "T", "A"]:
                slc.append("I")
                del dna[0:3]
            elif codon == ["C", "T", "T"] or ["C", "T", "C"] or ["C", "T", "A"] or ["T", "T", "A"] or ["T", "T", "G"]:
                slc.append("L")
                del dna[0:3]
            elif codon == ["G", "T", "T"] or ["G", "T", "C"] or ["G", "T", "A"] or ["G", "T", "G"]:
                slc.append("V")
                del dna[0:3]
            elif codon == ["T", "T", "T"] or ["T", "T", "C"]:
                slc.append("F")
                del dna[0:3]
            elif codon == ["A", "T", "G"]:
                slc.append("M")
                del dna[0:3]
            elif codon == ["T", "G", "T"] or ["T", "G", "C"]:
                slc.append("C")
                del dna[0:3]
            elif codon == ["G", "C", "T"] or ["G", "C", "C"] or ["G", "C", "A"] or ["G", "C", "G"]:
                slc.append("A")
                del dna[0:3]
            elif codon == ["G", "G", "T"] or ["G", "G", "C"] or ["G", "G", "A"] or ["G", "G", "G"]:
                slc.append("G")
                del dna[0:3]
            elif codon == ["C", "C", "T"] or ["C", "C", "C"] or ["C", "C", "A"] or ["C", "C", "G"]:
                slc.append("P")
                del dna[0:3]
            elif codon == ["A", "C", "T"] or ["A", "C", "C"] or ["A", "C", "A"] or ["A", "C", "G"]:
                slc.append("T")
                del dna[0:3]
            elif codon == ["T", "C", "T"] or ["T", "C", "C"] or ["T", "C", "G"] or ["A", "G", "T"] or ["A", "G", "C"]:
                slc.append("S")
                del dna[0:3]
            elif codon == ["T", "A", "T"] or ["T", "A", "C"]:
                slc.append("Y")
                del dna[0:3]
            elif codon == ["T", "G", "G"]:
                slc.append("W")
                del dna[0:3]
            elif codon == ["C", "A", "A"] or ["C", "A", "G"]:
                slc.append("Q")
                del dna[0:3]
            elif codon == ["A", "A", "T"] or ["A", "A", "C"]:
                slc.append("N")
                del dna[0:3]
            elif codon == ["C", "A", "T"] or ["C", "A", "C"]:
                slc.append("H")
                del dna[0:3]
            elif codon == ["G", "A", "A"] or ["G", "A", "C"]:
                slc.append("E")
                del dna[0:3]
            elif codon == ["G", "A", "T"] or ["G", "A", "C"]:
                slc.append("D")
                del dna[0:3]
            elif codon == ["A", "A", "A"] or ["A", "A", "G"]:
                slc.append("K")
                del dna[0:3]
            elif codon == ["C", "G", "T"] or ["C", "G", "C"] or ["C", "G", "A"] or ["C", "G", "G"] or \
                    ["A", "G",  "A"] or ["A", "G", "G"]:
                slc.append("R")
                del dna[0:3]
            elif codon == ["T", "A", "A"] or ["T", "A", "G"] or ["T", "G", "A"]:
                slc.append("Stop")
                del dna[0:3]
        else:
            break
    return slc


mutate_normal()
mutate_mutated()
print("...Welcome to the dna decoding app...")
dna = list(input("Please enter the dna sequence to decode: \n").upper())
print(str(translate(dna)))
