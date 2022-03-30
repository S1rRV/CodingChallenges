from collections import defaultdict

def getPalindrome(st):
    
    hmap = defaultdict(int)
    for i in range(len(st)):
        hmap[st[i]] += 1
    
    print(hmap)
    print(sorted(hmap.keys()))
        
    oddCount = 0
    
    for x in hmap:
        if (hmap[x] % 2 != 0):
            oddCount += 1
            oddChar = x
    
    if (oddCount > 1 or oddCount == 1 and len(st) %2 ==0):
        print(hmap)
        return "NO PALINDROME"
    
    firstHalf = ""
    secondHalf = ""
    
    for x in sorted(hmap.keys()):
        
        print("x is ", x)
        s = (hmap[x] // 2) * x
        
        print("s is = ", s)
        
        firstHalf = firstHalf + s 
        secondHalf = s + secondHalf
        
        print(firstHalf)
        print(secondHalf) 
    
    if (oddCount == 1):
        return (firstHalf + oddChar + secondHalf)
    else:
        return (firstHalf + secondHalf)
    
if __name__ == "__main__":
 
    s = "malayalam"
 
    print(getPalindrome(s))
