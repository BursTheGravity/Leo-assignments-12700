def commacode(l):
    ans = ""
    for i in range (len(l)):
        if i == len (l) - 1:
            ans += "and " + str(l[i])
        else:
            ans += str(l[i]) + ", "
    return ans

l1=['a','b','c']
print (commacode(l1))

l2 = [1,2,3]
print (commacode(l2))

l3 =[]
print (commacode(l3))