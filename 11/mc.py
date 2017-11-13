import random

def find_alphas(w):
    '''
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    '''
    all_letters=""
    for l in w:
        if l.isalpha():
            all_letters = all_letters + l
    return all_letters

def make_trigram_dict(wordlist):
    '''
    input: wordlist - list of alpha chars/words
    output: a dictionary containing every two "words" in the text with a list
            of words that appear after them in the text
    '''
    dict = {}
    
    for i in range(len(wordlist)-2):
        word1 = wordlist[i]
        word2 = wordlist[i+1]
        next_word = wordlist[i+2]
        #create a default empty list for new "words"
        dict.setdefault( (word1, word2), [] )
        #add the next word in the wordlist as a value for the word in dict
        dict[word1, word2].append(next_word)
    
    #accounts for the last word:
    #last_word = wordlist[len(wordlist)-1]
    #dict.setdefault(last_word, [])
    return dict

def read_txt_track_words(f):
    '''
    input: f - string representing a filename
    output: a dictionary with keys for words and values
            of the number of times each word occurs
    '''
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = find_alphas(w)
        l.append(w)
    
    #Make a trigram dictionary
    d = make_trigram_dict(l)
    
    return d

def generate_trigram_text(d, start_words, length = 50):
    wordlist = []
    next_words = start_words
    next_added_word = ""
    
    #initial words = 2 starting words:
    for word in next_words:
        wordlist.append(word)
    
    for i in range (length):
        #if no instances of the pair of words in next_words exist, break
        if next_words not in d:
            break
        #choose a random word from start_words 
        next_added_word = random.choice(d[next_words])
        wordlist.append(next_added_word)
        #create new next words list with last element of next_words and new word
        next_words = ( next_words[1], next_added_word )
        
    ans = " ".join(wordlist)
    return ans

#==========================RUN FUNCTIONS BELOW================================

#trigram dictionaries
hamlet = read_txt_track_words("hamlet.txt")
psalms = read_txt_track_words("psalms.txt")
sonnets = read_txt_track_words("sonnets.txt")

print("Hamlet trigram text:")
print(generate_trigram_text( hamlet, ('to', 'be') ))

print("\nPsalms trigram text:")
print(generate_trigram_text( psalms, ('blessed', 'is') ))

print("\nSonnets trigram text:")
print(generate_trigram_text( sonnets, ('as', 'the') ))
