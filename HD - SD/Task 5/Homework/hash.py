#   Create a new Python file in this folder called hash.py
#   Think about three celeberaties/famous people that you know.
#   Create a hash called hotMap, where the the KEYS are the name and surname of the person (ie a String), and the VALUE for each key is either the string 'hot' or
#   'not'
#   based on whether you think that person is hot or not!
#
#   Here's my hash..
#   hotMap = {
#       'EmmaWatson': 'Hot',
#       'JustinBieber': 'Not',
#       'LeoDiCaprio': 'Hot',
#   }
#
#   What does print hotMap['EmmaWatson'] return?

#Collecting user input
print("_ess_caA_ba, __s__B__b_r, M_g_nF_x, __l_o_by")
Map = input("Type the Celebs name and see if I agree with you: ")
#Setting up hash map
hotMap = {
    "JessicaAlba" : "Hot",
    "JustinBieber" : "Not",
    "MeganFox" : "Hot",
    "BillCosby" : "Not",
}
#Output operation
print(hotMap[Map])
    
