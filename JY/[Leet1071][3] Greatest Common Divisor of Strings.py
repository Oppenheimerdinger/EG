#1071. Greatest Common Divisor of Strings

def gcdOfStrings(str1, str2):
    if len(str1) <= len(str2):
        gcd = str1
    else:
        gcd = str2
    
    n = len(gcd)
    
    for k in range(n,0,-1):
        gcd = gcd[:k]  #gcd의 처음부터 k-1번째 글자까지 (길이가 k)
        if len(str1)%k ==0 and len(str2)%k==0:
            i = len(str1)//k
            j = len(str2)//k
            if gcd*i == str1 and gcd*j == str2:
                return gcd
            else:
                continue
    return ""


if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    result1 = gcdOfStrings(str1, str2)
    print(result1)
    
    str1 = "ABABAB"
    str2 = "ABAB"
    result2 = gcdOfStrings(str1, str2)
    print(result2)
    
    str1 = "LEET"
    str2 = "CODE"
    result3 = gcdOfStrings(str1, str2)
    print(result3)