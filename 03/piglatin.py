def piglatinify(s):
    ans = ""
    x = s[0:1].lower()
    if x in ("a","e","i","o","u"):
        ans = s + "ay"
    else:
        ans = s[1:].capitalize() + x + "ay"
    return ans

print ("Hello -> " + piglatinify('Hello'))
print ("Ello -> " + piglatinify('Ello'))
