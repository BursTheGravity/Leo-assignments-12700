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
#returns all alphabetical letters of word
#fix for: conjunctions

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
    return dict
#for every character in wordlist, keeps track of how many times each char appears

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
#function reads through a file and returns the frequency of every word

#=========================================================================

d = read_txt_track_words("hamlet.txt")
#print(d)

for i in d:
    print( i, ": ", d[i])

'''
NOTES:
v = list(d.values())
v.sort()
print(v)

#stemming: conovert similar words (make, makes, made, etc.) into the same word
#this creates a different count for said "main" word

#l=[x for x in range(10)]
#l = [c for c in "hello world"]
l=[k.upper() for k in d if d[k] > 5]
[ (x,y) for x in range(4) for y in range(5) ]
print (l)

test = {'lol': [1,2,3,4], 'two': [2,2,2]}
print(test)
'''