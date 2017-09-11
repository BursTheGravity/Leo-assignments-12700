s = "James Bond."
spc = s.find(" ")
length = len(s)
first = s[0:spc]
#checks if there is a period at the end
if (s[length-1:] == "."):
        last = s[spc+1:length-1]
else:
        last = s[spc+1:]
ans = last + ", " + first + " " + last + "."

print ans
