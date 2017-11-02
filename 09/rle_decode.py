def rle_decode(list):
    ans = ""
    i = 0
    while i < len(list):
        #if integer, then there will be a char following
        if isinstance(list[i], int):
            ans += list[i+1] * list[i]
            i += 2
        #otherwise, char is standalone, and only 1 copy of it
        else:
            ans += list[i]
            i += 1
    return ans
    
print(rle_decode([2,'a',3,'b','c',2,'d']))
print(rle_decode([2, 'a', 'b', 3, 'c', 'd', 2, 'e', 'a']))