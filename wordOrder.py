# The below function takes in a sentence that has numbers contained within each word. 
# The returned sentence at the end of the function's process, is the passed in sentence but in proper numerical order. 

def order(sentence):
    split_sentence = sentence.split(" ")
    new_sentence = []
    i = 1

    while len(split_sentence) >= i:
      string_number = str(i)
      for word in split_sentence:
          if string_number in word:
              new_sentence.append(word)
              i += 1
    

    result = " ".join(new_sentence)

    return result

order("fo3r i2s Thi1s m4e")

# Result when called above on line 22, is "Thi1s i2s fo3r m4e".
