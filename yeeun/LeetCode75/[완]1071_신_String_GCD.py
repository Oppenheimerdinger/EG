#2. 코딩의 신 빙의
"""
str1과 str2의 공약수들을 가지고 체크를 할거고, 공약수를 어떻게 판별할 것인가?
-> 더 길이 작은 애의 공약수들을 check를 할거임. len(str1)& len(str2)의 공약수가 1, 2, 3, 6이라면 
 
"""

def gcdOfStrings(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if l1 < l2:
        shorter = str1
        longer = str2
    else:
        shorter = str2
        longer = str1
    
    len_s = len(shorter)
    len_l = len(longer)
    #공약수 찾아서 비교하기
    for k in range(len_s, 0, -1):
        if len_s%k == 0 and len_l%k ==0:
            d_s = len_s//k
            d_l = len_l//k
            candidate = shorter[0:k]
            if candidate*d_s == shorter and candidate*d_l == longer:
                gcd = candidate
            else:
                gcd = ""
            return gcd
            

    

if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    k1 = gcdOfStrings(str1, str2)
    print(k1)

    str1 = "ABABAB"
    str2 = "ABAB"
    k2 = gcdOfStrings(str1, str2)
    print(k2)

    str1 = "LEET"
    str2 = "CODE"
    k3 = gcdOfStrings(str1, str2)
    print(k3)
        