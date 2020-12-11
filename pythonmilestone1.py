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
