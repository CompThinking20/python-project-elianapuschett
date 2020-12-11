import random
nouns = ["rose", "cathedral", "body", "sky", "lover", "friend"]

def create_poem(words):
  write = **
  word_number = random.randint (1, 3)
  for item in range(0, word_number):
    word_to_pop = random.randint(0, len(words) - 1)
    write +- words.pop(word_to_pop) + " "
  return write
  
print create_poem(nouns)

import random
nouns = ["darling", "foe", "lover", "friend", "forest" "catheral" "song" "story" "city" "light"]

def create_poem(words):
    poem = ""
    word_number = random.randint(1, 3)
    for item in range(0, word_number):
        word_to_pop = random.randint(0, len(words)-1)
        poem += words.pop(word_to_pop) + ""
    return poem

print create_poem(nouns)

#Here i used the text generator formula to start with the randomization of nouns.
#I will continue this for other types of words, then shuffle it all togehter.
#This method will randomly generate words from the above list, and I can also use it for others, like verbs.
