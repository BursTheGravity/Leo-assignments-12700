import random

story = '''
Once upon a time, there was a ADJ NOUN.
It loved to VERB all the time.
A ADJ NOUN came by one day to VERB with it.
The two were joined by a ADJ NOUN that loved to VERB all the time.
The three had no worries in the world, and would VERB everyday.

'''

nouns = ['dog','cat','bird','mouse','snake']
verbs =['run','jump','hide','crawl']
adjs =['big','small','tall','short']

def madlibs (story):
    #Split story by whitespace
    split_story = story.split()
    punc = ''',.?!:;()'''
    for i in range (len(split_story)):
        p = ''
        new_word = ''
        word = split_story[i]
        #punc checker
        if word[len(word)-1:] in punc:
            p = word[len(word)-1:]
            new_word = word[:len(word)-1]
        else:
            new_word = word
        #checks for keywords & replaces word
        if new_word == "NOUN":
            r = random.randrange(len(nouns))
            new_word = nouns[r]
        elif new_word == "VERB":
            r = random.randrange(len(verbs))
            new_word = verbs[r]
        elif new_word == "ADJ":
            r = random.randrange(len(adjs))
            new_word = adjs[r]
        #Re-adds to list
        split_story[i] = new_word + p
    #Joins split_story list back into a string
    new_story = (' ').join(split_story)
    return new_story

madlibstory = madlibs(story)
print (madlibstory)