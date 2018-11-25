#This is an example Python program.

#The purpose of this is to demonstrate the strength of the String data type.

#We have normal, single line strings:

name = "John"

#and multi-line strings;

bigStory = '''Alan Mathison Turing, OBE, FRS (pron.: /'tj??r??/ tewr-ing; 23 June 1912 – 7 June 1954), was a British mathematician, logician, cryptanalyst, and
computer scientist. He was highly influential in the development of computer science, giving a formalisation of the concepts of "algorithm" and "computation" with
the Turing machine, which can be considered a model of a general purpose computer.[1][2][3] Turing is widely considered to be the father of computer science and
artificial intelligence.[4]

During World War II, Turing worked for the Government Code and Cypher School (GC&CS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8,
the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an
electromechanical machine that could find settings for the Enigma machine.

After the war, he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined
Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers[5] and became interested in mathematical
biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov–Zhabotinsky reaction, which were
first observed in the 1960s.

Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female
hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest
determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British
Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated". As of May 2012 a private
member's bill was brought before the House of Lords which would grant Turing a statutory pardon if enacted.'''

print(bigStory)

#Note how we use ''' to define a multi-line String (preserves formatting in the String) and " " to define a normal string

#If we want formatting in a String we have to explicitly add it:

people = "Person 1 \n Person 2"

print(people) #Notice the line break between the two words. The \n character is invisible - it's a command to insert a new line.

wage = "Person 1: \t R123.22"

print(wage) #Notice the tab between the two words. The \t character is invisible - it's a command to insert a new tab space. 
