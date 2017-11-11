def getCount(inputStr): 
    vowel_list = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    for i in range(len(inputStr)):
        if inputStr[i] in vowel_list:
            num_vowels += 1
        print (num_vowels)   
    return num_vowels
