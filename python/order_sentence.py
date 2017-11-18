def find_number(str):
    for c in str:
        if(c.isdigit()):
            return (int(c)-1)

def order(sentence):
  sentence_split = sentence.split(' ')
  sentence_to_return = []
  length = len(sentence_split)
  # print (sentence_split)
  sentence_to_return = sentence_split
  for i in range(len(sentence_split)):
      place_in_sequence = (find_number(sentence_split[i])) 
      # print (sentence_split[i])
      temp = sentence_split[i]
      sentence_to_return.remove(sentence_split[i])
      print (sentence_to_return)
      print (place_in_sequence, sentence_split[i])
      sentence_to_return.insert(place_in_sequence, temp)
      print(sentence_to_return)
  return ' '.join(sentence_to_return)
  
  
order("is2 Thi1s T4est 3a")
