import math

#Low & Up alphabets to account for both lower and upper case letters
alph_low='abcdefghijklmnopqrstuvwxyz'
alph_up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Real stats list
real_stats = []

def encode_letter(c,r):
    #Lower Case:
    if c in alph_low:
        c_loc = alph_low.index(c)
        new_loc = c_loc + r
        #Only 26 letters in alphabet, so accounts for large ranges if necesary
        if new_loc > 25 or new_loc < -25:
            new_loc =  new_loc % 26
        return alph_low[new_loc]
    #Upper Case:
    elif c in alph_up:
        c_loc = alph_up.index(c)
        new_loc = c_loc + r
        #Only 26 letters in alphabet, so accounts for large ranges if necesary
        if new_loc > 25 or new_loc < -25:
            new_loc =  new_loc % 26
        return alph_up[new_loc]
    #If c is a non-letter, return itself
    else:
        return c

def encode_string(s,r):
    new_str = ''
    for x in s:
        new_str += encode_letter(x,r)
    return new_str

def full_encode (s):
    ans = ""
    for i in range (25):
        ans += str(i) + ": " + encode_string(s,i)
        ans += "\n"
    return ans

#==============================================================

#distance formula
def distance(l1,l2):
    '''
    Euclidean distance between l1 and l2. If the lists are of different
    lengths, go to the length of the shorter one
    '''
    length = len(l1)
    if length>len(l2):
        length = len(l2)
    sum = 0
    for i in range (length):
        sum = sum + (l1[i] - l2[i]) * (l1[i] - l2[i])
    d = math.sqrt(sum)
    return d

#build vector (list) of frequency of letters a-z within a given string
def build_frequency_vector(s):
    #count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    freq_vector = []
    #for every letter from a-z
    for letter in alph_low:
        #count how many times letter appears in given string
        letter_freq = s.count(letter)
        #divide by total letters to find frequency (out of 1.00)
        freq_vector.append(letter_freq / num_letters)
    #return entire list of frequencies, organized from a-z respectively
    return freq_vector

#print a readable version of frequency vector
def print_table(v):
    for i in range (len(alph_low)):
        print (alph_low[i] + ": " + str(v[i]))

def decode (s):
    ans = ""
    #keep track of lowest distance
    dist_tracker = 1.0
    #"decode" the string via rotational cipher (1-25)
    for i in range (len(alph_low)):
        #rotate string 26 times, one at a time
        rotated_str = encode_string(s, i)
        current_freq_vec = build_frequency_vector(rotated_str)
        dist = distance (real_stats, current_freq_vec)
        if dist < dist_tracker:
            dist_tracker = dist
            ans = rotated_str
    return ans

#================================================

def txt_real_stats():
    f = open("frankenstein.txt")
    s = f.read()
    f.close()
    
    c_loc = 0
    num_letters = 0
    
    #Removes all "\n"'s within the text
    story = s.split('\n')
    story = " ".join(story)
    letter_freq = []
    freq_vector = []
    
    #create 26 0's in letter_freq list
    for i in range (26): letter_freq.append(0)
    
    #count number of letters in the story
    for char in story:
        if char in alph_low or char in alph_up:
            num_letters += 1
    #print ('num letters: ' + str(num_letters))
    
    #run through letters in story, recording the frequency 
    for char in story:
        if char in alph_low:
            c_loc = alph_low.find(char)
        elif char in alph_up:
            c_loc = alph_up.find(char)
        letter_freq[c_loc] += 1
    #print (letter_freq)
    
    #create frequency vector
    for i in range (len(letter_freq)):
        freq_vector.append(letter_freq[i] / num_letters)
    
    return freq_vector

#run txt_real_stats(), set it to real_stats
real_stats = txt_real_stats()
#print("Real stats based on HTML text of Frankenstein by Mary Shelley: \n" + str(real_stats) + "\n")

test_str = "This is an actual legitimate sentence"
print ("Original string: " + test_str)
print ("Encoded string: " + encode_string(test_str, 3))
print ("Decoded string with new real_stats: " + decode(test_str))
'''
project gutenberg
download text, run through and create your own "real stats" based
on the letters in text instead
'''