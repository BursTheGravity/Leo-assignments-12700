#you can read a file into a big string using read
f = open("data.dat")
#f is now a file object and we can read from it
s = f.read()
f.close()
print(s)

#can be done in one line, but unable to close like this
s2 = open("data.dat").read()
print(s2)

#can now do things as a string
l = s2.split()
print(l)
l2 = s2.split("\n")
print(l2)

#can also simply split by readlines
l3 = open("data.dat").readlines()
print (l3)

f = open("data.dat")
for line in f:
    print (line)

s = open("data.dat").read()
for c in s:
    print(c)