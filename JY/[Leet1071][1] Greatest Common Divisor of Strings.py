#1071. Greatest Common Divisor of Strings [실패]
"""str1과 str2가 주어졌을 때, 
return largest string x, such that x divides both str1 and str2"""


"""
지윤's 접근
1. 여기서 구하려는 GCD는 concat해서 str1, str2가 되어야 함
2. 그렇다면 먼저, str1과 str2중 짧은 것을 GCD후보로 두고, 
3. 여기서 하나씩 졸여가면서 GCD가 맞는지 비교해보면 되지 않을까.
4. 하나씩 줄여갈 때는 맨 앞자리에서부터 하나씩 빼는 진행, 맨 뒤에서부터 하나씩 빼는 진행 모두 필요
5. gcd가 맞는지 비교해볼 때는 임의의 숫자 i,j를 하나씩 키워가면서
   gcd*i == str1 , gcd*j == str2인지를 보면 알 수 있을 것이다.
6. 
"""

def gcdOfStrings(self, str1, str2):
        # """
        # :type str1: str
        # :type str2: str
        # :rtype: str
        # """
    if len(str1) < len(str2):
        gcd = str1
    elif :
        gcd = str2
    
    # for k in range(len(gcd)):
    #     i, j = 1, 1
    #     while gcd*i != str1 and len(gcd)*i <= len(str1):
    #         i++
    #     while gcd*j != str2 and len(gcd)*j <= len(str2):
    #         j++
    
    for forward in range(len(gcd)):
        times_1 = len(str1)/len(gcd) 
        times_2 = len(str2)/len(gcd)
        check_list = [False, False]
        for i in range(1, times_1+1):
            if gcd*i == str1:
                check_list[0] = True
        for j in range(1, times_2+1):
            if gcd*j == str2:
                check_list[1] = True
        if check_list == [True, True]:
            return gcd
        else:
            gcd = gcd[forward+1:]

    for backward in range(len(gcd)):
        times_1 = len(str1)/len(gcd) 
        times_2 = len(str2)/len(gcd)
        check_list = [False, False]
        for i in range(1, times_1+1):
            if gcd*i == str1:
                check_list[0] = True
        for j in range(1, times_2+1):
            if gcd*j == str2:
                check_list[1] = True
        if check_list == [True, True]:
            return gcd
        else:
            gcd = gcd[0:len(gcd)-backward+1]
            
    return ""  #다 돌아도 return gcd 못 했을 때는 "" 반환



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