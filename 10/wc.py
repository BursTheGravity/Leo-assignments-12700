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

def make_dict_of_nextwords(wordlist):
    '''
    input: wordlist - list of alpha chars/words
    output: a dictionary containing every "word" in the text with a list of
            words that appear after it in the text
    '''
    dict = {}
    for i in range(len(wordlist)-1):
        curr_word = wordlist[i]
        next_word = wordlist[i+1]
        #create a default empty list for new "words"
        dict.setdefault(curr_word, [])
        #add the next word in the wordlist as a value for the word in dict
        dict[curr_word].append(next_word)
    #accounts for the last word
    last_word = wordlist[len(wordlist)-1]
    dict.setdefault(last_word, [])
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
    #splitting like this tracks words; taking out the '.split()' part tracks letters
        w = w.lower()
        w = find_alphas(w)
        l.append(w)
    d = make_dict_of_nextwords(l)
    return d

#=========================================================================

d = read_txt_track_words("hamlet.txt")
print(d)

for i in d:
    print( i, ": ", d[i])
