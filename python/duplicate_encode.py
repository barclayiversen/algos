# This algo is supposed to return parens based on whether the character in the string appears more than once or not (I think)
# I believe this came from codewars

test_a = "din"
test_b = "recede"
from collections import OrderedDict

def duplicate_encode(word):
    word = word.lower()
    letter_count = OrderedDict()
    string_to_print = ""
    for letter in word:
        letter_count[letter] = word.count(letter)
        if letter_count[letter] == 1:
            string_to_print += "("
        else:
            string_to_print += ")"
    print (string_to_print)
    return string_to_print
    
    
duplicate_encode(test_b)

#test_a.count()
