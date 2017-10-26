
def divide (A, B, u):
    ans = float((u/A)*B)
    if ans < 0:
        ans = 0
    return int(ans)

print(divide(5, 10, 1)) #ans = 2
print(divide(2, 8, 2)) #ans = 8
print(divide(3, 7, 1)) #only 6/7 of cake taken, allowing for 2 people; ans = 2
print(divide(10, 1, 1)) #10 cakes per person, only 1 cake to split; ans = 0
print(divide(-5, 10, 1)) #negative num, so ans = 0

print("\n")

def encode(s):
    ans = []
    curr_letter = ""
    curr_sum = 1
    for char in s:
        if (char != curr_letter):
            #add sum and char onto list:
            #add sum if it's not 1
            if curr_sum != 1:
                ans.append(curr_sum)
            #add char if not empty char
            if curr_letter != "":
                ans.append(curr_letter)
            #reset values:
            curr_letter = char
            curr_sum = 0
        curr_sum += 1
    #append both values once more at the end
    if curr_sum != 1:
        ans.append(curr_sum)
    if curr_letter != "":
        ans.append(curr_letter)
        
    return ans
    
print(encode("")) #should just be an empty list
print(encode("aaaaa")) #should be [5,'a']
print(encode("aabcccdeea")) #should be [2, 'a', 'b', 3, 'c', 'd', 2, 'e', 'a']
print(encode("!!!!@##BBAAA11223")) #should be [4, '!', '@', 2, '#', 2, 'B', 3, 'A', 2, '1', 2, '2', '3']

print("\n")

def score(w):
    letter_vals = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
    ans = 0
    for char in w:
        ans += letter_vals.get(char, 0)
    return ans
    
print(score('hello')) #ans = 8
print(score('queen')) #ans = 14
print(score('')) #ans = 0
print(score('123!?*&')) #ans = 0
print(score('abcdefghijklmnopqrstuvwxyz')) #ans = 87
