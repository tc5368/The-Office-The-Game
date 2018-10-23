
from items import items
from npc import chars
#Replace the filter words with this keep words
keep_words = ['go','take','drop','north','south','west','east','inventory','exit','everyone','look','where']

for names in items:
    keep_words.append(names)    #This just adds all the possible items and characters to the keep_words
for names in chars:             #list to make sure they are recognised by the parser for where and look
    keep_words.append(names)

def filter_words(words):
    output = []
    for w in words:                         #This is the filter words should be changed to keep words
        if w in keep_words:                 #instead of removing words not needed.
            output.append(w)                #but at the moment works by looping through the words in the
    return output                           #list and then only adding ones not in skip words to the output list

def remove_punct(text):
    no_punct = ""
    for char in text:                       #This function loops through every single character in a string
        if char.isalpha() or char == ' ':   #If its a letter or a space then it is added to an output string
            no_punct = no_punct + char      #then return the output string
    return no_punct


def normalise_input(user_input):
    return filter_words(remove_punct(user_input).lower().split())             #This runs remove punctuation function and then
                                                                              #reaplcs all the cahacrtes to lower case.  
                                                                              #then it splits then words into a list and returns it.

