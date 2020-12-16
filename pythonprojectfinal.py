import random
nouns = ["rose", "cathedral", "body", "sky", "lover", "friend"]

def create_poem(words):
  poem = ""
  word_number = random.randint (1, 3)
  for item in range(0, word_number):
    word_to_pop = random.randint(0, len(words) - 1)
    poem +- words.pop(word_to_pop) + " "
  return poem
  
print create_poem(nouns)

import random
noun = ["darling", "foe", "forest", "song", "story", "city", "light"]

def create_write(words):
    write = ""
    word_number = random.randint(1, 3)
    for item in range(0, word_number):
        word_to_pop = random.randint(0, len(words)-1)
        poem += words.pop(word_to_pop) + " "
    return write

print create_write(noun)

import random
adjectvies = ["dazzling", "gentle", "dark", "defeated", "bitter", "east", "west", "bright"]

def create_phrase(words):
  phrase = ""
  word_number = random.randint(2, 4)
  for item in range(0, word_number):
    word_to_pop = random.randint(0, len(words)-1)
    phrase += words.pop(word_to_pop) + " "
  return phrase
  
print create_phrase(adjectvies)

import random 
verbs = ["accuse", "choose", "entail", "love", "forbid", "desire", "flown", "slit"]

def create_term(words):
  term = ""
  word_number = random.randint(2, 4)
  for item in range(0, word_number):
    word_to_pop = random.randint(0, len(words)-1)
    term += words.pop(word_to_pop) + " "
  return term
  
print create_term(verbs)

import random
adverbs = ["equally", "lively", "very", "there", "outside", "well", "grimly", "away"]

def create_part(words):
  part = ""
  word_number = random.randint(1, 3)
  for item in range(0, word_number):
    word_to_pop = random.randint(0, len(words)-1)
    part += words.pop(word.to.pop) + " "
  return part
  
print create_part(adverbs)

print create_poem(nouns), print create_write(noun), create_phrase(adjectvies), create_term(verbs), reate_part(adverbs)

