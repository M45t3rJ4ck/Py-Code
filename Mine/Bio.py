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
    codon = {"I": [["A", "T", "T"], ["A", "T", "C"], ["A", "T", "A"]],
             "L": [["C", "T", "T"], ["C", "T", "C"], ["C", "T", "A"], ["T", "T", "A"], ["T", "T", "G"]],
             "V": [["G", "T", "T"], ["G", "T", "C"], ["G", "T", "A"], ["G", "T", "G"]],
             "F": [["T", "T", "T"], ["T", "T", "C"]],
             "M": ["A", "T", "G"],
             "C": [["T", "G", "T"], ["T", "G", "C"]],
             "A": [["G", "C", "T"], ["G", "C", "C"], ["G", "C", "A"], ["G", "C", "G"]],
             "G": [["G", "G", "T"], ["G", "G", "C"], ["G", "G", "A"], ["G", "G", "G"]],
             "P": [["C", "C", "T"], ["C", "C", "C"], ["C", "C", "A"], ["C", "C", "G"]],
             "T": [["A", "C", "T"], ["A", "C", "C"], ["A", "C", "A"], ["A", "C", "G"]],
             "S": [["T", "C", "T"], ["T", "C", "C"], ["T", "C", "G"], ["A", "G", "T"], ["A", "G", "C"]],
             "Y": [["T", "A", "T"], ["T", "A", "C"]],
             "W": ["T", "G", "G"],
             "Q": [["C", "A", "A"], ["C", "A", "G"]],
             "N": [["A", "A", "T"], ["A", "A", "C"]],
             "H": [["C", "A", "T"], ["C", "A", "C"]],
             "E": [["G", "A", "A"], ["G", "A", "C"]],
             "D": [["G", "A", "T"], ["G", "A", "C"]],
             "K": [["A", "A", "A"], ["A", "A", "G"]],
             "R": [["C", "G", "T"], ["C", "G", "C"], ["C", "G", "A"], ["C", "G", "G"], ["A", "G", "A"], ["A", "G", "G"]],
             "Stop": [["T", "A", "A"], ["T", "A", "G"], ["T", "G", "A"]]}
    while len(dna) != 0:
        if codon.values == dna[0:3]:
            slc.append(codon.keys())
            del dna[0:3]
        return slc


dna = list(input("Enter your sequence to convert: \n").upper())
print(str(translate(dna)))
