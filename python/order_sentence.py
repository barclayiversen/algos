def find_number(str):
    #print (str)
    for c in str:
        if(c.isdigit()):

            return (int(c)-1)

# def order(sentence):
#   sentence_split = sentence.split(' ')
#   sentence_to_return = []
#   length = len(sentence_split)
#   print (sentence_split)
#   sentence_to_return = sentence_split
#   for i in range(len(sentence_split)):
#       place_in_sequence = (find_number(sentence_split[i]))
#       print ("sentence_split[i]", sentence_split[i], "i: ", i)
#       temp = sentence_split[i]
#       print ("sentence_split again: ",sentence_split, "sentence_to_return: ", sentence_to_return)
#       sentence_to_return.remove(sentence_split[i])
#       print ("sentence_split 3: ",sentence_split, "sentence_to_return: ", sentence_to_return)
#       #print (place_in_sequence, sentence_split[i])
#       sentence_to_return.insert(place_in_sequence, temp)
#       #print('sentence to return: ',sentence_to_return)
#   return ' '.join(sentence_to_return)
  

def order(sentence):
  sentence_split = sentence.split(' ')
  idx_obj = {}
  for word in range(len(sentence_split)):
      print ('sentence[word]: ',sentence_split[word])
      index = find_number(sentence_split[word])
      print (word, index)
      idx_obj[index] = sentence_split[word]
      #print idx_obj
  for key in sorted(idx_obj.iterkeys()):
      print "%s: %s" % (key, idx_obj[key])
  print idx_obj
      
      
#order("is2 Thi1s T4est 3a")
order("4of Fo1r pe6ople g3ood th5e the2")
