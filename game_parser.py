

#This is words to remove from the input string
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

#Replace the filter words with this keep words
keep_words = ['go','take','drop','north','south','west','east']


def filter_words(words):
    output = []
    for w in words:                         #This is the filter words should be changed to keep words
        if w not in skip_words:             #instead of removing words not needed.
            output.append(w)         #but at the moment works by looping through the words in the
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

