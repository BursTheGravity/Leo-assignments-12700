import math

#Low & Up alphabets to account for both lower and upper case letters
alph_low='abcdefghijklmnopqrstuvwxyz'
alph_up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Real stats of frequency of letters in English words sorted a-z
real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]


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
        
'''
Run through decryptions one by one
whenever a decryption has a smaller distance to real_stats,
change current decryption
This way, no need to keep track of every single decryption
'''
        
    

#print (encode_letter('t',3))
#print (encode_string('hello',1))
#print (full_encode('Hello World!!!'))
s = 'this is an actual legitimate sentence'
print ("original sentence: " + s)
s2 = encode_string(s, 5)
print ("encoded sentence: " + s2)
print ("decoded sentence: " + decode(s2))
