def freq (n, l):
    ans = 0
    for i in range (len(l)):
        if l[i] == n:
            ans += 1
    return ans

def min (l):
    ans = l[0]
    for i in range (len(l)):
        if l[i] < ans:
            ans = l[i]
    return ans

def mode (l):
    nums = []
    for i in range (len(l)):
        if l[i] not in nums:
            nums.append(l[i])
    ans = nums[0]
    for num in nums:
        if freq(num, l) > freq(ans, l):
            ans = num
    return ans

