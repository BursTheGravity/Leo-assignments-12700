def encode_letter(c,r):
    #Low & Up alphabets to account for both lower and upper case letters
    alph_low='abcdefghijklmnopqrstuvwxyz'
    alph_up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
    for i in range (26):
        ans += str(i) + ": " + encode_string(s,i)
        ans += "\n"
    return ans

#print (encode_letter('t',3))
#print (encode_string('hello',1))
print (full_encode('Hello World!!!'))