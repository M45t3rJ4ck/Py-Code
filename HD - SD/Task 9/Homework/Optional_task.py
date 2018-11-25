# == Optional Challenge ==
#   Go to http://en.wikipedia.org/wiki/Garden_path_sentence#Parsing
#   Read about the different Parsing strategies.
#   Add a comment at the bottom of your program explaining which parsing strategy you think an AI like Siri (the iPhone
#   4 talking robot) uses and why? What kind of data structures might you suggest is used in this process? Go to
#   http://www.inf.ed.ac.uk/teaching/courses/inf2a/slides/2011_inf2a_L22_slides.pdf and read up till #slide 16 of this
#   University of Edinburgh slide on Human Parsing. How do you think humans eyes respond when encountering a Garden Path
#   sentence and what type of parsing (serial or parallel) do you think this is evidence of?


"""

Parsing strategy for AI:        Semantic Serial Left-Corner with Backtracking

The sentence or words needs to make sense at the end...so the logic behind the structure of the language based on the words needs to flow in a
direction with each word clarifying the previous word as to not end up with a double meaning, but a more correct one in terms of spelling or
grammar by logical default. Working from the left corner would be faster and estimated to be correct mostly, that is where the right corner or
backtracking as a back-up is ideal...it allows for each word to be analyzed be it's own the way back to a point stability before continuing onto
the next most plausible approach, at which point a possible input from user on best option to take can be requested and I think it is the same way
human eyes responds to garden path sentences.

"""
