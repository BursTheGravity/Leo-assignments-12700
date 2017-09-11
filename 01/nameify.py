s = "fried chicken"
spc = s.find(" ")
word1 = s[0:spc]
word2 = s[spc+1:]
ans = word1.capitalize() + " " + word2.capitalize()

print ans
